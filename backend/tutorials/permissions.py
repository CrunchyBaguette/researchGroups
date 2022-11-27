from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from backend.tutorials.models import Tutorial, Rating


class IsTutorialOwner(BasePermission):
    """Grants permission to a tutorial owner"""

    def has_object_permission(self, request: Request, view: APIView, obj: Tutorial) -> bool:
        is_owner = obj.owner.id == request.user.id
        return is_owner


class IsTutorialEditor(BasePermission):
    """Grants permission to a tutorial editor"""

    def has_object_permission(self, request: Request, view: APIView, obj: Tutorial) -> bool:
        is_editor = obj.editors.contains(obj)
        return is_editor


class IsRatingAuthor(BasePermission):
    """Grants permission to a rating author"""

    def has_object_permission(self, request: Request, view: APIView, obj: Rating) -> bool:
        is_author = obj.author.id == request.user.id
        return is_author
