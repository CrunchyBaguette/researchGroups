from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["password", "groups", "last_login", "user_permissions"]

class UserSerializerName(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user"] = UserSerializer(user).data
        return token


class SendMailSerializer(serializers.Serializer):
    sender = serializers.EmailField(write_only=True)
    receivers = serializers.ListField(child=serializers.EmailField(), allow_empty=False)
    subject = serializers.CharField(max_length=255, allow_blank=False)
    body = serializers.CharField(max_length=1000, allow_blank=False)
