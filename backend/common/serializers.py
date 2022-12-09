from collections import OrderedDict

from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed
import jwt


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=8, write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        first_name = attrs.get("first_name", "")
        last_name = attrs.get("last_name", "")
        password = attrs.get("password", "")
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        attrs["is_active"] = False
        validate_password(password, user)

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["password", "token"]

    def validate(self, attrs: OrderedDict):
        try:
            token_str = attrs.get("token")
            token = jwt.decode(token_str, settings.SECRET_KEY, algorithms=["HS256"])
            User.objects.get(id=token["user_id"])
            return attrs

        except ObjectDoesNotExist as exc:
            raise AuthenticationFailed("User does not exist") from exc
        except jwt.ExpiredSignatureError as exc:
            raise AuthenticationFailed("Token expired") from exc
        except jwt.DecodeError as exc:
            raise AuthenticationFailed("Invalid token") from exc
