from typing import Any
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.request import Request
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer, CustomTokenObtainPairSerializer, SendMailSerializer
from backend.research_groups.models import ResearchGroup, ResearchGroupUser
from backend.projects.models import Project
from backend.research_groups.serializers import ResearchGroupSerializer
from backend.projects.serializers import ProjectSerializer
from backend.common.views import PermissionPolicyMixin
from backend.utilsx.mail.EmailBuilder import EmailBuilder


class UserViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes_per_method = {
        "researchGroups": [
            IsAuthenticated,
        ],
        "adminResearchGroups": [
            IsAuthenticated,
        ],
        "projects": [
            IsAuthenticated,
        ],
    }

    @action(detail=True, methods=["get"])
    def researchGroups(self, request, pk=None):  # pylint: disable=unused-argument
        user = self.get_object()
        researchGroups = ResearchGroup.objects.all().order_by("name")
        researchGroupData = ResearchGroupSerializer(researchGroups, many=True)
        userResarchGroups = []

        for researchGroup in researchGroupData.data:
            if user.email in researchGroup["members"]:
                userResarchGroups.append(researchGroup)

        return Response(userResarchGroups)

    @action(detail=True, methods=["get"])
    def adminResearchGroups(self, request, pk=None):  # pylint: disable=unused-argument
        user = self.get_object()
        researchGroupUsers = ResearchGroupUser.objects.filter(person=user, role__in=["mod", "cr"]).all()
        userResearchGroups = [researchGroupUser.research_group for researchGroupUser in researchGroupUsers]
        researchGroupSerializer = ResearchGroupSerializer(userResearchGroups, many=True)
        return Response(researchGroupSerializer.data)

    @action(detail=True, methods=["get"])
    def projects(self, request, pk=None):  # pylint: disable=unused-argument
        user = self.get_object()
        projects = Project.objects.all().order_by("name")
        projectData = ProjectSerializer(projects, many=True)
        userProjects = []

        for project in projectData.data:
            if user.email in project["members"]:
                userProjects.append(project)

        return Response(userProjects)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(("POST",))
@permission_classes((IsAuthenticated,))
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
    except KeyError:
        return Response("You need to include your refresh token", status=400)

    try:
        token = RefreshToken(refresh_token)
    except TokenError:
        return Response("You need to provide a valid refresh token", status=400)

    token.blacklist()
    logout(request)

    return Response("Successful logout", status=200)


class SendEmailView(generics.GenericAPIView):
    serializer_class = SendMailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        emails_sent = 0

        for r in data["receivers"]:
            email = EmailBuilder(sender=data["sender"], subject=data["subject"], message=data["body"], recipient=r)
            emails_sent += email.send()

        return Response({"message": f"Sent {emails_sent} emails successfully"}, status=status.HTTP_200_OK)
