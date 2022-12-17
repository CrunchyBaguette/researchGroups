from typing import Any, Type
from logging import getLogger
from datetime import timedelta
import jwt
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from backend.users.serializers import UserSerializer
from backend.common.serializers import RegisterSerializer, ResetPasswordSerializer, SetNewPasswordSerializer
from backend.common.utils import (
    generate_registration_link,
    get_registration_email,
    generate_reset_pass_link,
    get_reset_pass_email,
)

logger = getLogger(__name__)


class PermissionPolicyMixin(APIView):
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
        user = request.data["user"]
        if request.data["joining"]:
            created_user = User.objects.filter(is_active=False, email=user["email"]).first()
            if not created_user:
                return Response({}, status=status.HTTP_404_NOT_FOUND)
            created_user.username = user["username"]
            created_user.first_name = user["first_name"]
            created_user.last_name = user["last_name"]
            created_user.set_password(user["password"])
            created_user.save()
        else:
            serializer: RegisterSerializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            created_user: User = serializer.save()

        token = RefreshToken.for_user(created_user).access_token
        token.lifetime = timedelta(days=1)

        link = generate_registration_link(token)
        email = get_registration_email(created_user, link)
        if email.send() == 1:
            logger.info("Email to user %s with register link sent", created_user.username)
        else:
            logger.warning("Could not send email with register link for user %s", created_user.username)

        return Response(request.data["user"], status=status.HTTP_201_CREATED)

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
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
            logger.warning("Token expired")
            return Response({"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            logger.warning("Invalid token")
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordRequestView(generics.GenericAPIView):
    serializer_class: ResetPasswordSerializer = ResetPasswordSerializer  # type: ignore
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: ResetPasswordSerializer = self.get_serializer_class()(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        try:
            user = User.objects.get(email=email)
            token = RefreshToken.for_user(user).access_token
            token.lifetime = timedelta(minutes=30)

            link = generate_reset_pass_link(token)
            mail = get_reset_pass_email(user, link)
            if mail.send() == 1:
                logger.info("Email to user %s with register link sent", user.username)
                return Response({"message": "Successfully send email with reset link"})

            logger.warning("Could not send email with register link for user %s", user.username)
            return Response({"error": "Email with reset link has not been sent"})

        except ObjectDoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: SetNewPasswordSerializer = self.get_serializer_class()(data=request.data)  # type: ignore
        serializer.is_valid(raise_exception=True)
        user = request.user
        if request.user.is_authenticated:
            user.set_password(str(serializer.validated_data["password"]))
            user.save()
            user_data = UserSerializer(user).data
            return Response({"message": "Successfully changed password", "user": user_data}, status=status.HTTP_200_OK)

        try:
            token = serializer.validated_data["token"]
            payload = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"])
            found_user: User = User.objects.get(id=payload["user_id"])
            found_user.set_password(str(serializer.validated_data["password"]))
            found_user.save()
            user_data = UserSerializer(found_user).data

            return Response({"message": "Successfully changed password", "user": user_data}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            logger.warning("Token expired")
            return Response({"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.DecodeError:
            logger.warning("Invalid token")
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist as exc:
            raise AuthenticationFailed("User does not exist") from exc

    def get_serializer_class(self) -> Type[ResetPasswordSerializer | SetNewPasswordSerializer]:
        if self.request.method == "POST":
            return ResetPasswordSerializer
        if self.request.method == "PUT":
            return SetNewPasswordSerializer
        return ResetPasswordSerializer
