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

        ownerMember = ResearchGroupUser.objects.filter(
            research_group__name=request.data["name"],
            person__email=request.user.email,
        ).first()
        ownerMember.role = "cr"
        ownerMember.save()

        return response


class ResearchGroupPostViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroupPost.objects.all()
    serializer_class = ResearchGroupPostSerializer

    @action(detail=False, methods=["get"])
    def grouped(self, request):
        researchGroup = request.query_params.get("researchGroup", None)
        if not researchGroup:
            return Response(
                {"researchGroup": ["'researchGroup' parameter is required."]},
                status=400,
            )
        postsQueryset = ResearchGroupPost.objects.filter(research_group=researchGroup).order_by("added").all()
        serializer = self.get_serializer(postsQueryset, many=True)
        return Response({"researchGroup": researchGroup, "posts": serializer.data})
