from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.research_groups.serializers import ResearchGroupSerializer
from backend.research_groups.models import ResearchGroup

from backend.common.views import PermissionPolicyMixin


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

        for member in members:
            if not User.objects.filter(email=member).exists():
                User.objects.create_user(
                    username=member.split("@")[0],
                    password=member.split("@")[0],
                    email=member,
                )
        return super().create(request, *args, **kwargs)
