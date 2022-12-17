from rest_framework import serializers
from django.contrib.auth.models import User
from backend.utilsx.serializers import QuerySerializerMixin
from backend.projects.models import (
    Project,
    ProjectPost,
    ProjectUser,
    ProjectLink,
    ProjectDisk,
)
from backend.users.serializers import UserSerializerName


class ProjectSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, slug_field="email", queryset=User.objects.all())
    project_owner = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())

    RELATED_FIELDS = ["project_owner"]
    PREFETCH_FIELDS = ["members"]

    class Meta:
        model = Project
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation


class ProjectUserSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())
    project = serializers.SlugRelatedField(slug_field="id", queryset=Project.objects.all())

    RELATED_FIELDS = ["project", "person"]

    class Meta:
        model = ProjectUser
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["role"] = instance.get_role_display()
        return representation


class ProjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPost
        fields = "__all__"


class ProjectPostSerializerWithUser(serializers.ModelSerializer):
    author = UserSerializerName(many=False, read_only=True)

    class Meta:
        model = ProjectPost
        fields = "__all__"


class ProjectLinkSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    users = serializers.SlugRelatedField(many=True, slug_field="email", queryset=User.objects.all())

    PREFETCH_FIELDS = ["users"]

    class Meta:
        model = ProjectLink
        fields = "__all__"


class ProjectDiskSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    users = serializers.SlugRelatedField(many=True, slug_field="email", queryset=User.objects.all())

    PREFETCH_FIELDS = ["users"]

    class Meta:
        model = ProjectDisk
        fields = "__all__"
