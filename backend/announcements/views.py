from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from backend.announcements.models import Announcement
from backend.announcements.serializers import AnnouncementSerializer
from backend.common.views import PermissionPolicyMixin


class AnnouncementViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ]
    }
