from rest_framework import serializers
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer
from backend.tutorials.models import Tutorial, Rating
from backend.utilsx.serializers import QuerySerializerMixin


class TutorialSerializer(serializers.ModelSerializer):
    owner = UserSerializer(partial=True)
    editors = UserSerializer(many=True, partial=True)
    editable = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Tutorial
        fields = "__all__"
        read_only_fields = ["created", "edited", "editable"]


class RatingTutorialSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELD = ["author"]

    class Meta:
        model = Rating
        fields = "__all__"


class AddEditorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        write_only_fields = ["id", "username", "email"]