from collections import Counter

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from backend.common.views import PermissionPolicyMixin
from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
)
from backend.projects.serializers import (
    ProjectSerializer,
    ProjectUserSerializer,
    ProjectPostSerializer,
    ProjectPostSerializerWithUser,
)


class ProjectUserViewSet(viewsets.ModelViewSet):
    queryset = ProjectUser.objects.all().order_by("created")
    serializer_class = ProjectUserSerializer
    permission_classes = [AllowAny]

    roleCodes = {
        "Owner": "own",
        "Moderator": "mod",
        "Member": "mem",
    }

    @action(detail=False, methods=["get"])
    def projectMembers(self, request):
        projectId = request.query_params.get("projectId", None)
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        members = self.get_queryset()
        projectMembers = members.filter(project__id=projectId).all()
        serializer = self.get_serializer(projectMembers, many=True)
        return Response({"project": projectId, "members": serializer.data})

    @action(detail=False, methods=["post"])
    def updateMembers(self, request):
        projectId = request.data["projectId"]
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        members = self.get_queryset()
        newMembers = request.data["members"]

        newMembersRoles = [newMember["role"] for newMember in newMembers]
        if Counter(newMembersRoles)["Owner"] != 1:
            raise APIException("Projekt musi posiadać dokładnie jedengo twórcę")

        projectMembers = members.filter(project__id=projectId).all()
        projectMembers.delete()

        newMembersResponseList = []

        for newMember in newMembers:
            newMemberSerialized = ProjectUserSerializer(
                data={
                    "project": projectId,
                    "person": newMember["person"],
                    "role": self.roleCodes.get(newMember["role"]),
                }
            )
            if newMemberSerialized.is_valid():
                newMemberSerialized.save()
                newMembersResponseList.append(newMember)
            if newMember["role"] == "Owner":
                project = Project.objects.filter(id=projectId).first()
                newMemberObject = User.objects.filter(email=newMember["person"]).first()
                project.project_owner = newMemberObject
                project.save()
        return Response({"project": projectId, "members": newMembersResponseList})


# Create your views here.
class ProjectViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("name")
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ]
    }

    categoryCodes = {"Default": "def"}

    def create(self, request, *args, **kwargs):
        # Obecnie, w przypadku gdy nie ma użytkownika z podanym mailem, tworzony jest
        # nowy ale później można tu zaimplementować rozsyłanie maili
        members = request.data["members"]
        members.append(self.request.user.email)

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

    def update(self, request, *args, **kwargs):
        request.data["category"] = self.categoryCodes.get(request.data["category"])
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        project = request.query_params.get("project", None)
        if not project:
            return Response(
                {"project": ["'project' parameter is required."]},
                status=400,
            )
        projectsQueryset = self.get_queryset()
        projectsData = projectsQueryset.filter(project=project).all()
        projectsSerializer = self.get_serializer(projectsData, many=True)
        return Response(
            {
                "project": project,
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
        participation = ProjectPost.objects.filter(author_id=userId, project_id=project)
        return Response({"project": project, "isParticipant": participation.exists(), "posts": serializer.data})

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer_class = ProjectPostSerializerWithUser
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = serializer_class(post)
        return Response(serializer.data)
