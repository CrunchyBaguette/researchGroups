from typing import Any
from logging import getLogger
from datetime import timedelta
import jwt
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from backend.utilsx.mail.EmailBuilder import EmailBuilder
from backend.users.serializers import UserSerializer
from .serializers import RegisterSerializer


logger = getLogger(__name__)


class PermissionPolicyMixin(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permission_classes_per_method = None

    def check_permissions(self, request):
        try:
            # This line is heavily inspired from `APIView.dispatch`.
            # It returns the method associated with an endpoint.
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if handler and self.permission_classes_per_method and self.permission_classes_per_method.get(handler.__name__):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        created_user: User = serializer.save()

        token = RefreshToken.for_user(created_user).access_token
        token.lifetime = timedelta(days=1)

        current_site = get_current_site(request).domain
        relative_link = reverse("register")
        absurl = f"http://{current_site}{relative_link}?token={token}"

        email = (
            EmailBuilder(settings.EMAIL_HOST_USER)
            .add_text(get_email_body_for_user(created_user, absurl))
            .add_receiver(created_user.email)
            .build_django_mail()
        )
        if email.send() == 1:
            logger.info("Email to user %s with register link sent", created_user.username)
        else:
            logger.warning("Could not send email with register link for user %s", created_user.username)

        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user: User = User.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
                user_data = UserSerializer(user).data
                return Response(
                    {"message": "Successfully activated account", "user": user_data}, status=status.HTTP_200_OK
                )
            user_data = UserSerializer(user).data
            return Response(
                {"error": "Account already activated", "user": user_data}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


def get_email_body_for_user(user: User, link: str) -> str:
    return f"Hi {user.first_name} \nUse this link to activate your account: {link}"
