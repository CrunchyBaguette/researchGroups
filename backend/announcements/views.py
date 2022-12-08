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
        ],
        "partial_update": [
            IsAuthenticated,
        ],
    }

    def update(self, request, *args, **kwargs):
        print(request.data["ann_type"])
        match request.data["ann_type"]:
            case "Poszukiwanie sponsora":
                request.data["ann_type"] = "sponsor"
            case "Poszukiwanie nowych członków":
                request.data["ann_type"] = "rekrutacja"
            case "Poszukiwanie osób do projektu":
                request.data["ann_type"] = "projekt"
        return super().update(request, *args, **kwargs)
