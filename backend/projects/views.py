from collections import Counter
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from backend.projects.serializers import (
    ProjectSerializer,
    ProjectUserSerializer,
    ProjectPostSerializer,
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
        return Response({"researchGroup": projectId, "members": newMembersResponseList})


# Create your views here.
class ProjectViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
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

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        project = request.query_params.get("project", None)
        if not project:
            return Response(
                {"project": ["'project' parameter is required."]},
                status=400,
            )
        postsQueryset = ProjectPost.objects.filter(project=project).order_by("added").all()
        serializer = self.get_serializer(postsQueryset, many=True)
        return Response({"project": project, "posts": serializer.data})
