from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


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
        validate_password(password, user)

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
