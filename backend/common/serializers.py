from collections import OrderedDict

from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str


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

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["password", "token", "uidb64"]

    def validate(self, attrs: OrderedDict):
        try:
            token = attrs.get("token")
            uidb64 = attrs.get("uidb64")

            user_id = force_str(urlsafe_base64_decode(uidb64))
            user: User = User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("The reset link is invalid")

            return attrs

        except ObjectDoesNotExist:
            raise AuthenticationFailed("User does not exist")

