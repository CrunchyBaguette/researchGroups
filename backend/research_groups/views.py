from collections import Counter

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from backend.research_groups.serializers import (
    ResearchGroupUserSerializer,
    ResearchGroupSerializer,
    ResearchGroupPostSerializer,
    ResearchGroupLinkSerializer,
    ResearchGroupDiskSerializer,
    ResearchGroupPostSerializerWithUser,
)
from backend.research_groups.models import (
    ResearchGroup,
    ResearchGroupPost,
    ResearchGroupUser,
    ResearchGroupLink,
    ResearchGroupDisk,
)

from backend.common.views import PermissionPolicyMixin
from backend.common.utils import get_research_group_email, generate_research_group_link


class ResearchGroupUserViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupUser.objects.all().order_by("created")
    serializer_class = ResearchGroupUserSerializer
    permission_classes = [AllowAny]

    roleCodes = {
        "Member": "mem",
        "Moderator": "mod",
        "Creator": "cr",
    }

    @action(detail=False, methods=["get"])
    def groupMembers(self, request):
        researchGroupId = request.query_params.get("researchGroupId", None)
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        members = self.get_queryset()
        researchGroupMembers = members.filter(research_group__id=researchGroupId).all()
        serializer = self.get_serializer(researchGroupMembers, many=True)
        return Response({"researchGroup": researchGroupId, "members": serializer.data})

    @action(detail=False, methods=["post"])
    def updateMembers(self, request):
        researchGroupId = request.data["researchGroupId"]
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        members = self.get_queryset()
        newMembers = request.data["members"]

        newMembersRoles = [newMember["role"] for newMember in newMembers]
        if Counter(newMembersRoles)["Creator"] != 1:
            raise APIException("Koło naukowe musi posiadać dokładnie jedengo twórcę")

        researchGroupMembers = members.filter(research_group__id=researchGroupId).all()
        researchGroupMembers.delete()

        newMembersResponseList = []

        for newMember in newMembers:
            newMemberSerialized = ResearchGroupUserSerializer(
                data={
                    "research_group": researchGroupId,
                    "person": newMember["person"],
                    "role": self.roleCodes.get(newMember["role"]),
                }
            )
            if newMemberSerialized.is_valid():
                newMemberSerialized.save()
                newMembersResponseList.append(newMember)
            if newMember["role"] == "Creator":
                researchGroup = ResearchGroup.objects.filter(id=researchGroupId).first()
                newMemberObject = User.objects.filter(email=newMember["person"]).first()
                researchGroup.group_owner = newMemberObject
                researchGroup.save()
        return Response({"researchGroup": researchGroupId, "members": newMembersResponseList})


# Create your views here.
class ResearchGroupViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = ResearchGroup.objects.all().order_by("name")
    serializer_class = ResearchGroupSerializer
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ],
        "partial_update": [
            IsAuthenticated,
        ],
    }

    categoryCodes = {
        "Matematyka": "math",
        "Medycyna": "med",
        "Chemia": "chem",
    }

    def create(self, request, *args, **kwargs):
        # Obecnie, w przypadku gdy nie ma użytkownika z podanym mailem, tworzony jest
        # nowy ale później można tu zaimplementować rozsyłanie maili
        member_emails = request.data["members"]
        member_emails.append(self.request.user.email)

        for member_email in member_emails:
            if not User.objects.filter(email=member_email).exists():
                User.objects.create_user(
                    username=member_email.split("@")[0],
                    password=member_email.split("@")[0],
                    email=member_email,
                )

        response = super().create(request, *args, **kwargs)

        ownerMember = ResearchGroupUser.objects.filter(
            research_group__id=response.data["id"], person__email=self.request.user.email
        ).first()
        ownerMember.role = "cr"
        ownerMember.save()

        return response

    def update(self, request, *args, **kwargs):
        request.data["category"] = self.categoryCodes.get(request.data["category"])
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["post"])
    def email(self, request, *args, **kwargs):
        link = generate_research_group_link(request.data["researchGroupId"])
        email = get_research_group_email(
            request.data["creator"],
            request.data["sender"],
            request.data["subject"],
            request.data["text"],
            request.data["research_group_name"],
            link,
        )
        email.send()
        return Response(status=status.HTTP_201_CREATED)


class ResearchGroupPostViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupPost.objects.all()
    serializer_class = ResearchGroupPostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        serializer_class = ResearchGroupPostSerializerWithUser
        researchGroup = request.query_params.get("researchGroup", None)
        userId = request.query_params.get("userId", None)
        if not researchGroup:
            return Response(
                {"researchGroup": ["'researchGroup' parameter is required."]},
                status=400,
            )
        if not userId:
            return Response(
                {"userId": ["'userId' parameter is required."]},
                status=400,
            )
        postsQueryset = self.queryset.filter(research_group=researchGroup).order_by("added")
        serializer = serializer_class(postsQueryset, many=True)
        participation = ResearchGroupUser.objects.filter(person_id=userId, research_group_id=researchGroup)
        return Response(
            {"researchGroup": researchGroup, "isParticipant": participation.exists(), "posts": serializer.data}
        )

    def retrieve(self, request, *args, pk=None, **kwargs):
        serializer_class = ResearchGroupPostSerializerWithUser
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = serializer_class(post)
        return Response(serializer.data)


class ResearchGroupLinkViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupLink.objects.all()
    serializer_class = ResearchGroupLinkSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def groupLinks(self, request):
        researchGroupId = request.data["researchGroupId"]
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        links = self.get_queryset()
        researchGroupLinks = links.filter(research_group=researchGroupId).all()
        serializer = self.get_serializer(researchGroupLinks, many=True)
        return Response({"researchGroup": researchGroupId, "links": serializer.data})

    @action(detail=False, methods=["post"])
    def updateLinks(self, request):
        researchGroupId = request.data["researchGroupId"]
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        links = self.get_queryset()
        newLinks = request.data["links"]

        researchGroupLinks = links.filter(research_group=researchGroupId).all()
        researchGroupLinks.delete()

        newLinksResponseList = []

        for newLink in newLinks:
            newLinkSerialized = self.get_serializer(
                data={
                    "research_group": researchGroupId,
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

        return Response({"researchGroup": researchGroupId, "links": newLinksResponseList})


class ResearchGroupDiskViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupDisk.objects.all()
    serializer_class = ResearchGroupDiskSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def groupDisks(self, request):
        researchGroupId = request.data["researchGroupId"]
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        disks = self.get_queryset()
        researchGroupDisks = disks.filter(research_group=researchGroupId).all()
        serializer = self.get_serializer(researchGroupDisks, many=True)
        return Response({"researchGroup": researchGroupId, "disks": serializer.data})

    @action(detail=False, methods=["post"])
    def updateDisks(self, request):
        researchGroupId = request.data["researchGroupId"]
        if not researchGroupId:
            return Response(
                {"researchGroupId": ["'researchGroupId' parameter is required."]},
                status=400,
            )
        disks = self.get_queryset()
        newDisks = request.data["disks"]

        researchGroupDisks = disks.filter(research_group=researchGroupId).all()
        researchGroupDisks.delete()

        newDisksResponseList = []

        for newDisk in newDisks:
            newDiskSerialized = self.get_serializer(
                data={
                    "research_group": researchGroupId,
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

        return Response({"researchGroup": researchGroupId, "disks": newDisksResponseList})
