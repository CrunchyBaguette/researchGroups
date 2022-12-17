from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.announcements.models import Announcement
from backend.announcements.serializers import AnnouncementSerializer
from backend.common.views import PermissionPolicyMixin
from backend.common.utils import get_announcement_email, generate_announcement_link


class AnnouncementViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny]
    permission_classes_per_method = {
        "create": [
            IsAuthenticated,
        ],
        "partial_update": [
            IsAuthenticated,
        ],
    }

    def update(self, request, *args, **kwargs):
        match request.data["ann_type"]:
            case "Poszukiwanie sponsora":
                request.data["ann_type"] = "sponsor"
            case "Poszukiwanie nowych członków":
                request.data["ann_type"] = "rekrutacja"
            case "Poszukiwanie osób do projektu":
                request.data["ann_type"] = "projekt"
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["post"])
    def email(self, request, *args, **kwargs):
        link = generate_announcement_link(request.data["annId"])
        email = get_announcement_email(
            request.data["author"], request.data["sender"], request.data["text"], request.data["annTitle"], link
        )
        email.send()
        return Response(status=status.HTTP_201_CREATED)
