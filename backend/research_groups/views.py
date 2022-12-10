from collections import Counter
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.research_groups.serializers import (
    ResearchGroupUserSerializer,
    ResearchGroupSerializer,
    ResearchGroupPostSerializer, ResearchGroupPostSerializerWithUser,
)
from backend.research_groups.models import (
    ResearchGroup,
    ResearchGroupPost,
    ResearchGroupUser,
)

from backend.common.views import PermissionPolicyMixin


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
        postsQueryset = self.queryset.filter(research_group=researchGroup).order_by("added").all()
        serializer = serializer_class(postsQueryset, many=True)
        participation = ResearchGroupUser.objects.filter(person_id=userId, research_group_id=researchGroup)
        return Response({"researchGroup": researchGroup, "isParticipant": participation.exists(), "posts": serializer.data})

    def retrieve(self, request, pk=None, *args, **kwargs):
        serializer_class = ResearchGroupPostSerializerWithUser
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = serializer_class(post)
        return Response(serializer.data)