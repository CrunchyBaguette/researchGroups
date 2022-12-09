from rest_framework import serializers
from django.contrib.auth.models import User

from backend.users.serializers import UserSerializerName
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


class ResearchGroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroupUser
        fields = "__all__"


class ResearchGroupPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchGroupPost
        fields = "__all__"


class ResearchGroupPostSerializerWithUser(serializers.ModelSerializer):
    author = UserSerializerName(many=False, read_only=True)

    class Meta:
        model = ResearchGroupPost
        fields = "__all__"
