from typing import Any
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.request import Request
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer, CustomTokenObtainPairSerializer, SendMailSerializer
from backend.utilsx.mail.EmailBuilder import EmailBuilder


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(("POST",))
@permission_classes((IsAuthenticated,))
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
    except KeyError:
        return Response("You need to include your refresh token", status=400)

    try:
        token = RefreshToken(refresh_token)
    except TokenError:
        return Response("You need to provide a valid refresh token", status=400)

    token.blacklist()
    logout(request)

    return Response("Successful logout", status=200)


class SendEmailView(generics.GenericAPIView):
    serializer_class = SendMailSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        emails_sent = 0

        for r in data["receivers"]:
            email = EmailBuilder(data["sender"]).add_subject(data["subject"]).add_text(data["body"])
            email.add_receiver(r)
            emails_sent += email.build_django_mail().send()

        return Response({"message": f"Sent {emails_sent} emails successfully"}, status=status.HTTP_200_OK)
