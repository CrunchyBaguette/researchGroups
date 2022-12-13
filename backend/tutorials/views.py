from typing import Any
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from backend.projects.models import Project
from backend.users.views import PermissionPolicyMixin
from backend.tutorials.models import Tutorial, Rating
from backend.tutorials.serializers import TutorialSerializer
from backend.tutorials.permissions import IsTutorialEditor, IsTutorialOwner


class TutorialViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.all().order_by("created")
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [IsAuthenticated],
        "partial_update": [IsTutorialEditor | IsTutorialOwner],
        "update": [IsTutorialEditor | IsTutorialOwner],
        "destroy": [IsTutorialOwner]
    }

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        pass

    @action()
    def add_editors(self):
        pass
