from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model, logout
from backend.users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from backend.research_groups.models import ResearchGroup, ResearchGroupUser
from backend.projects.models import Project
from backend.research_groups.serializers import ResearchGroupSerializer
from backend.projects.serializers import ProjectSerializer
from backend.common.views import PermissionPolicyMixin


class UserViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
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
        researchGroups = ResearchGroup.objects.all()
        researchGroupData = ResearchGroupSerializer(researchGroups, many=True)
        userResarchGroups = []

        for researchGroup in researchGroupData.data:
            if user.email in researchGroup["members"]:
                userResarchGroups.append(researchGroup)

        return Response(userResarchGroups)

    @action(detail=True, methods=["get"])
    def adminResearchGroups(self, request, pk=None):  # pylint: disable=unused-argument
        user = self.get_object()
        researchGroupUsers = ResearchGroupUser.objects.filter(person=user, role="mod").all()
        userResearchGroups = [researchGroupUser.research_group for researchGroupUser in researchGroupUsers]
        researchGroupSerializer = ResearchGroupSerializer(userResearchGroups, many=True)
        return Response(researchGroupSerializer.data)

    @action(detail=True, methods=["get"])
    def projects(self, request, pk=None):  # pylint: disable=unused-argument
        user = self.get_object()
        projects = Project.objects.all()
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
