from rest_framework import serializers
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer
from backend.tutorials.models import Tutorial, Rating
from backend.utilsx.serializers import QuerySerializerMixin


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    editors = UserSerializer(many=True)

    class Meta:
        model = Tutorial
        fields = "__all__"


class RatingTutorial(QuerySerializerMixin, serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELD = ["author"]

    class Meta:
        model = Rating
        fields = "__all__"
