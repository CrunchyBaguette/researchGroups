from rest_framework import serializers

from backend.research_groups.models import ResearchGroup
from backend.users.serializers import UserSerializer


class ResearchGroupSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    group_owner = UserSerializer()

    class Meta:
        model = ResearchGroup
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation
