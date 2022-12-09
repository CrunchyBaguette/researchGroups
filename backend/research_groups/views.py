from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.research_groups.serializers import (
    ResearchGroupUserSerializer,
    ResearchGroupSerializer,
    ResearchGroupPostSerializer,
)
from backend.research_groups.models import (
    ResearchGroup,
    ResearchGroupPost,
    ResearchGroupUser,
)

from backend.common.views import PermissionPolicyMixin


class ResearchGroupUserViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupUser.objects.all()
    serializer_class = ResearchGroupUserSerializer


# Create your views here.
class ResearchGroupViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = ResearchGroup.objects.all()
    serializer_class = ResearchGroupSerializer
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ]
    }

    def create(self, request, *args, **kwargs):
        # Obecnie, w przypadku gdy nie ma użytkownika z podanym mailem, tworzony jest
        # nowy ale później można tu zaimplementować rozsyłanie maili
        member_emails = request.data["members"]

        for member_email in member_emails:
            if not User.objects.filter(email=member_email).exists():
                User.objects.create_user(
                    username=member_email.split("@")[0],
                    password=member_email.split("@")[0],
                    email=member_email,
                )

        return super().create(request, *args, **kwargs)


class ResearchGroupPostViewSet(viewsets.ModelViewSet):

    queryset = ResearchGroupPost.objects.all()
    serializer_class = ResearchGroupPostSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def grouped(self, request):
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
        participantion = ResearchGroupUser.objects.filter(person_id=userId).filter(research_group_id=researchGroup)
        postsQueryset = ResearchGroupPost.objects.filter(research_group=researchGroup).order_by("added").all()
        serializer = self.get_serializer(postsQueryset, many=True)
        isParticipant = False
        if(participantion):
            isParticipant = True
        return Response({"researchGroup": researchGroup, "isParticipant": isParticipant, "posts": serializer.data})

    # def retrieve(self, request, pk):
