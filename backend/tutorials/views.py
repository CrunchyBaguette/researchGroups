from typing import Any

from django.db.models import QuerySet, Q
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from backend.users.views import PermissionPolicyMixin
from backend.tutorials.models import Tutorial
from backend.tutorials.serializers import TutorialSerializer, TutorialEditSerializer
from backend.tutorials.permissions import IsTutorialEditor, IsTutorialOwner


class TutorialViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Tutorial.objects.filter(is_public=True, is_draft=False).order_by("edited")
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [IsAuthenticated],
        "partial_update": [IsTutorialEditor | IsTutorialOwner],
        "update": [IsTutorialEditor | IsTutorialOwner],
        "destroy": [IsTutorialOwner],
    }

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: TutorialEditSerializer = self.get_serializer(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["owner"] = request.user
        if request.user.id not in serializer.validated_data["editors"]:
            editors = serializer.validated_data.get("editors", [])
            editors.append(request.user)
            serializer.validated_data["editors"] = editors
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: TutorialSerializer = self.get_serializer(self.get_object())  # type: ignore
        tutorial = serializer.data
        if request.user.is_authenticated:
            for editor in tutorial["editors"]:
                if editor["id"] == request.user.id:
                    tutorial["editable"] = True
                    break
        return Response(tutorial)

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer: TutorialSerializer = self.get_serializer(queryset, many=True)  # type: ignore
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
        if self.action in ("list", "retrieve", "partial_update"):
            if projectId := self.request.GET.get("projectId", None):
                if self.request.user.is_authenticated:
                    return (
                        Tutorial.objects.filter(
                            Q(project_guide__project=projectId)
                            & Q(project_guide__project__members=self.request.user.id)
                        )
                        .exclude(Q(is_draft=True) & ~Q(editors=self.request.user.id))
                        .order_by("edited")
                    )

                return Tutorial.objects.filter(
                    Q(project_guide__is_public=True) & Q(project_guide__project=projectId) & Q(is_draft=False)
                ).order_by("edited")

            if researchGroupId := self.request.GET.get("researchGroupId", None):
                if self.request.user.is_authenticated:
                    return (
                        Tutorial.objects.filter(
                            Q(research_group_guide__research_group=researchGroupId)
                            & Q(research_group_guide__research_group__members=self.request.user.id)
                        )
                        .exclude(Q(is_draft=True) & ~Q(editors=self.request.user.id))
                        .order_by("edited")
                    )

                return Tutorial.objects.filter(
                    Q(research_group_guide__is_public=True)
                    & Q(research_group_guide__research_group=researchGroupId)
                    & Q(is_draft=False)
                ).order_by("edited")

            if self.request.user.is_authenticated:
                q = (
                    Tutorial.objects.filter(
                        Q(is_public=True)  # Jest publiczny
                        | Q(research_group_guide__research_group__members=self.request.user.id)  # Należy do kółka
                        | Q(project_guide__project__members=self.request.user.id)  # Jest w projekcie
                    )
                    .exclude(  # jest w kółku, ale nie jest edytorem a jest to draft
                        Q(research_group_guide__research_group__members=self.request.user.id)
                        & ~Q(editors=self.request.user.id)
                        & Q(is_draft=True)
                    )
                    .exclude(  # jest w projekcie, ale nie jest edytorem draftu
                        Q(project_guide__project__members=self.request.user.id)
                        & ~Q(editors=self.request.user.id)
                        & Q(is_draft=True)
                    )
                    .exclude(  # Ani nie jest w projekcie, ani w kółku a jest to draft
                        ~Q(research_group_guide__research_group__members=self.request.user.id)
                        & ~Q(project_guide__project__members=self.request.user.id)
                        & Q(is_draft=True)
                        & ~Q(editors=self.request.user.id)
                    )
                )
                return q.order_by("edited")

        return Tutorial.objects.filter(is_public=True, is_draft=False).order_by("created")
