from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ["password", "groups", "last_login", "user_permissions"]

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


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
