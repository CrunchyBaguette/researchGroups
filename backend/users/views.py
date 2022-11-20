from backend.users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model, logout


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
