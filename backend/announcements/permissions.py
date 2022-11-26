from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from backend.announcements.models import Announcement


class IsAnnouncementAuthor(BasePermission):
    """Grant permission to author of a announcement"""

    def has_object_permission(
        self, request: Request, view: APIView, obj: Announcement
    ) -> bool:
        is_author = obj.author == request.user
        return is_author
