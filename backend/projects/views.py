from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from backend.projects.serializers import (
    ProjectSerializer,
    ProjectUserSerializer,
    ProjectPostSerializer, ProjectPostSerializerWithUser,
)
from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
)

from backend.common.views import PermissionPolicyMixin


class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all()
    serializer_class = ProjectUserSerializer


# Create your views here.
class ProjectViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ]
    }

    def create(self, request, *args, **kwargs):
        # Obecnie, w przypadku gdy nie ma użytkownika z podanym mailem, tworzony jest
        # nowy ale później można tu zaimplementować rozsyłanie maili
        members = request.data["members"]

        if not request.user.email in members:
            members.append(request.user.email)

        for member in members:
            if not User.objects.filter(email=member).exists():
                User.objects.create_user(
                    username=member.split("@")[0],
                    password=member.split("@")[0],
                    email=member,
                )

        response = super().create(request, *args, **kwargs)

        ownerMember = ProjectUser.objects.filter(
            project__name=request.data["name"],
            person__email=request.user.email,
        ).first()
        ownerMember.role = "own"
        ownerMember.save()

        return response

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        researchGroup = request.query_params.get("researchGroup", None)
        if not researchGroup:
            return Response(
                {"researchGroup": ["'researchGroup' parameter is required."]},
                status=400,
            )
        projectsQueryset = self.get_queryset()
        projectsData = projectsQueryset.filter(research_group=researchGroup).all()
        projectsSerializer = self.get_serializer(projectsData, many=True)
        return Response(
            {
                "researchGroup": researchGroup,
                "projects": projectsSerializer.data,
            }
        )


class ProjectPostViewSet(viewsets.ModelViewSet):
    queryset = ProjectPost.objects.all()
    serializer_class = ProjectPostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        serializer_class = ProjectPostSerializerWithUser
        project = request.query_params.get("project", None)
        userId = request.query_params.get("userId", None)
        if not project:
            return Response(
                {"project": ["'project' parameter is required."]},
                status=400,
            )
        if not userId:
            return Response(
                {"userId": ["'userId' parameter is required."]},
                status=400,
            )
        postsQueryset = ProjectPost.objects.filter(project=project).order_by("added").all()
        serializer = serializer_class(postsQueryset, many=True)
        participation = ProjectPost.objects.filter(author_id=userId).filter(project_id=project)
        isParticipant = False
        if (participation):
            isParticipant = True
        return Response({"project": project, "isParticipant": isParticipant, "posts": serializer.data})

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer_class = ProjectPostSerializerWithUser
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = serializer_class(post)
        return Response(serializer.data)
