from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import ResearchGroup, ResearchGroupPost, ResearchGroupPostComment


class IsResearchGroupMember(BasePermission):
    """Grants permission if user is member of researchGroup"""

    def has_permission(self, request: Request, view: APIView) -> bool:
        is_member = ResearchGroup.objects.filter(members=request.user).exists()
        return is_member


class IsResearchGroupModerator(BasePermission):
    """Grants permission if user is moderator of researchGroup"""

    def has_object_permission(
        self, request: Request, view: APIView, obj: ResearchGroup
    ) -> bool:
        is_moderator = obj.members.filter(
            members=request.user, researchgroupuser__role="mod"
        ).exists()
        return is_moderator


class IsResearchGroupOwner(BasePermission):
    """Grants permission if user is ResearchGroup owner"""

    def has_object_permission(
        self, request: Request, view: APIView, obj: ResearchGroup
    ) -> bool:
        is_owner = obj.group_owner == request.user
        return is_owner


class IsGroupPostAuthor(BasePermission):
    """Grants permission if user is owner of a post on group"""

    def has_object_permission(
        self, request: Request, view: APIView, obj: ResearchGroupPost
    ) -> bool:
        is_owner = obj.author == request.user
        return is_owner


class IsGroupPostCommentAuthor(BasePermission):
    """Grants permission if user is owner of a comment on post on group"""

    def has_object_permission(
        self, request: Request, view: APIView, obj: ResearchGroupPostComment
    ) -> bool:
        is_owner = obj.author == request.user
        return is_owner
