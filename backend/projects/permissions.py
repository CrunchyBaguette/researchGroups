from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from backend.projects.models import Project, ProjectPost, ProjectPostComment


class IsProjectMember(BasePermission):
    """Grants permission if user is a project member"""

    def has_object_permission(self, request: Request, view: APIView, obj: Project) -> bool:
        is_member = Project.members.filter(id=request.user.id).exists()  # type: ignore
        return is_member


class IsProjectModerator(BasePermission):
    """Grants permission if user is moderator of a project"""

    def has_object_permission(self, request: Request, view: APIView, obj: Project) -> bool:
        is_moderator = obj.members.filter(id=request.user.id, researchgroupuser__role="mod").exists()  # type: ignore
        return is_moderator


class IsProjectOwner(BasePermission):
    """Grants permission if user is owner of a project"""

    def has_object_permission(self, request: Request, view: APIView, obj: Project) -> bool:
        is_owner = obj.members.filter(id=request.user.id, researchgroupuser__role="own").exists()  # type: ignore
        return is_owner


class IsProjectPostAuthor(BasePermission):
    """Grants permission to author of a project post"""

    def has_object_permission(self, request: Request, view: APIView, obj: ProjectPost) -> bool:
        is_author = obj.author.id == request.user.id
        return is_author


class IsProjectCommentAuthor(BasePermission):
    """Grants permission to author of comment on project post"""

    def has_object_permission(self, request: Request, view: APIView, obj: ProjectPostComment) -> bool:
        is_author = obj.author.id == request.user.id
        return is_author
