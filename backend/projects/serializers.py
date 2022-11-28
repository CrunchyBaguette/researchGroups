from rest_framework import serializers

from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
)

from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(
        many=True, slug_field="email", queryset=User.objects.all()
    )

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
