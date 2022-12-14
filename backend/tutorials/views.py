from typing import Any

from django.db.models import QuerySet
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from backend.projects.models import Project
from backend.research_groups.models import ResearchGroup
from backend.users.views import PermissionPolicyMixin
from backend.tutorials.models import Tutorial, Rating
from backend.tutorials.serializers import TutorialSerializer, TutorialEditSerializer
from backend.tutorials.permissions import IsTutorialEditor, IsTutorialOwner


class TutorialViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_public=True).order_by("created")
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [IsAuthenticated],
        "partial_update": [IsTutorialEditor | IsTutorialOwner],
        "update": [IsTutorialEditor | IsTutorialOwner],
        "destroy": [IsTutorialOwner],
    }

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: TutorialEditSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["owner"] = request.user
        if request.user.id not in serializer.validated_data["editors"]:
            editors = serializer.validated_data.get("editors", [])
            editors.append(request.user)
            serializer.validated_data["editors"] = editors
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer: TutorialSerializer = self.get_serializer(queryset, many=True)
        if request.user.is_authenticated:
            is_editor_of = Tutorial.objects.filter(editors=request.user)
            for tut in serializer.data:
                if is_editor_of.filter(id=tut["id"]).exists():
                    tut["editable"] = True
        return Response(serializer.data)

    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action in ["create", "update", "partial_update"]:
            return TutorialEditSerializer

        return TutorialSerializer

    def get_queryset(self) -> QuerySet:
        if self.action == "list":
            if self.request.user.is_authenticated:
                return Tutorial.objects.filter(is_public=True).order_by("created")
            else:
                if projectId := self.request.GET.get("projectId", None):
                    project: Project = Project.objects.get(id=projectId)
                    return project.guides.filter(is_public=True)
                elif researchGroupId := self.request.GET.get("researchGroupId", None):
                    research_group: researchGroupId = ResearchGroup.objects.get(id=researchGroupId)
                    return research_group.guides.filter(is_public=True)

        return Tutorial.objects.filter(is_public=True).order_by("created")
