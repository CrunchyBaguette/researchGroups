import random
import string
from collections import Counter

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core import mail
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from backend.projects.serializers import (
    ProjectSerializer,
    ProjectUserSerializer,
    ProjectPostSerializer,
    ProjectLinkSerializer,
    ProjectDiskSerializer,
    ProjectPostSerializerWithUser,
)
from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
    ProjectLink,
    ProjectDisk,
)
from backend.utilsx.mail.EmailBuilder import send_messages_conn
from backend.common.utils import (
    generate_join_link,
    get_join_project_email,
)
from backend.users.serializers import UserSerializer

from backend.common.views import PermissionPolicyMixin
from backend.common.utils import get_project_email, generate_project_link


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
            raise APIException("Projekt musi posiada?? dok??adnie jedengo tw??rc??")

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

    categoryCodes = {
        "Matematyka": "math",
        "Medycyna": "med",
        "Chemia": "chem",
    }

    def create(self, request, *args, **kwargs):
        member_emails = request.data["members"]
        member_emails.append(self.request.user.email)

        new_users = []

        for member_email in member_emails:
            if not User.objects.filter(email=member_email).exists():
                randUsername = "".join(random.choice(string.ascii_letters) for x in range(150))
                randPass = "".join(random.choice(string.ascii_letters) for x in range(150))
                serializer = UserSerializer(
                    data={"username": randUsername, "email": member_email, "password": randPass, "is_active": False}
                )
                serializer.is_valid(raise_exception=True)
                new_users.append(serializer.save())

        response = super().create(request, *args, **kwargs)

        ownerMember = ProjectUser.objects.get(
            project__id=response.data["id"],
            person__email=self.request.user.email,
        )
        ownerMember.role = "own"
        ownerMember.save()

        send_emails = []

        for new_user in new_users:
            link = generate_join_link(new_user.email)
            send_emails.append(get_join_project_email(new_user.email, response.data["name"], link))

        send_messages_conn(send_emails, mail.get_connection())

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

    @action(detail=False, methods=["post"])
    def email(self, request, *args, **kwargs):
        link = generate_project_link(request.data["projectId"])
        email = get_project_email(
            request.data["owner"],
            request.data["sender"],
            request.data["subject"],
            request.data["text"],
            request.data["project_name"],
            link,
        )
        email.send()
        return Response(status.HTTP_201_CREATED)


class ProjectPostViewSet(viewsets.ModelViewSet):
    queryset = ProjectPost.objects.order_by("-edited").all()
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
        postsQueryset = self.queryset.filter(project=project)
        serializer = serializer_class(postsQueryset, many=True)
        participation = ProjectUser.objects.filter(person_id=userId, project_id=project)
        return Response({"project": project, "isParticipant": participation.exists(), "posts": serializer.data})

    def retrieve(self, request, *args, pk=None, **kwargs):
        serializer_class = ProjectPostSerializerWithUser
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = serializer_class(post)
        return Response(serializer.data)


class ProjectLinkViewSet(viewsets.ModelViewSet):
    queryset = ProjectLink.objects.all()
    serializer_class = ProjectLinkSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def projectLinks(self, request):
        projectId = request.data["projectId"]
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        links = self.get_queryset()
        projectLinks = links.filter(project=projectId).all()
        serializer = self.get_serializer(projectLinks, many=True)
        return Response({"project": projectId, "links": serializer.data})

    @action(detail=False, methods=["post"])
    def updateLinks(self, request):
        projectId = request.data["projectId"]
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        links = self.get_queryset()
        newLinks = request.data["links"]

        projectLinks = links.filter(project=projectId).all()
        projectLinks.delete()

        newLinksResponseList = []

        for newLink in newLinks:
            newLinkSerialized = self.get_serializer(
                data={
                    "project": projectId,
                    "link": newLink["link"],
                    "name": newLink["name"],
                    "is_public": newLink["is_public"],
                    "users": newLink["users"],
                }
            )
            if newLinkSerialized.is_valid():
                newLinkSerialized.save()
                newLinksResponseList.append(newLink)
            else:
                print(newLinkSerialized.errors)

        return Response({"project": projectId, "links": newLinksResponseList})


class ProjectDiskViewSet(viewsets.ModelViewSet):
    queryset = ProjectDisk.objects.all()
    serializer_class = ProjectDiskSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def projectDisks(self, request):
        projectId = request.data["projectId"]
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        disks = self.get_queryset()
        projectDisks = disks.filter(project=projectId).all()
        serializer = self.get_serializer(projectDisks, many=True)
        return Response({"project": projectId, "disks": serializer.data})

    @action(detail=False, methods=["post"])
    def updateDisks(self, request):
        projectId = request.data["projectId"]
        if not projectId:
            return Response(
                {"projectId": ["'projectId' parameter is required."]},
                status=400,
            )
        disks = self.get_queryset()
        newDisks = request.data["disks"]

        projectDisks = disks.filter(project=projectId).all()
        projectDisks.delete()

        newDisksResponseList = []

        for newDisk in newDisks:
            newDiskSerialized = self.get_serializer(
                data={
                    "project": projectId,
                    "link": newDisk["link"],
                    "name": newDisk["name"],
                    "is_public": newDisk["is_public"],
                    "users": newDisk["users"],
                }
            )
            if newDiskSerialized.is_valid():
                newDiskSerialized.save()
                newDisksResponseList.append(newDisk)
            else:
                print(newDiskSerialized.errors)

        return Response({"project": projectId, "disks": newDisksResponseList})
