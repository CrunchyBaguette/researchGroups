from rest_framework import serializers
from django.contrib.auth.models import User
from backend.utilsx.serializers import QuerySerializerMixin
from backend.research_groups.models import (
    ResearchGroup,
    ResearchGroupPost,
    ResearchGroupUser,
)


class ResearchGroupSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, slug_field="email", queryset=User.objects.all())
    group_owner = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELDS = ["group_owner"]
    PREFETCH_FIELDS = ["members"]

    class Meta:
        model = ResearchGroup
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation


class ResearchGroupUserSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    person = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())
    research_group = serializers.SlugRelatedField(slug_field="id", queryset=ResearchGroup.objects.all())

    RELATED_FIELDS = ["research_group", "person"]

    class Meta:
        model = ResearchGroupUser
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["role"] = instance.get_role_display()
        return representation


class ResearchGroupPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroupPost
        fields = "__all__"
