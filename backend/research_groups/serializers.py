from rest_framework import serializers
from backend.users.serializers import UserSerializer
from backend.research_groups.models import (
    ResearchGroup,
    ResearchGroupPost,
    ResearchGroupUser,
)


class ResearchGroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    group_owner = UserSerializer()

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
