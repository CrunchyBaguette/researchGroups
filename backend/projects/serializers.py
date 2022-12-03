from rest_framework import serializers
from django.contrib.auth.models import User
from backend.utilsx.serializers import QuerySerializerMixin
from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
)


class ProjectSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, slug_field="email", queryset=User.objects.all())
    project_owner = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELDS = ["project_owner"]
    PREFETCH_FIELDS = ["members"]

    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation


class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = "__all__"


class ProjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPost
        fields = "__all__"
