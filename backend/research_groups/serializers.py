from rest_framework import serializers

from backend.research_groups.models import ResearchGroup
from django.contrib.auth.models import User


class ResearchGroupSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(
        many=True, slug_field="email", queryset=User.objects.all()
    )

    class Meta:
        model = ResearchGroup
        fields = [
            "id",
            "name",
            "about_us",
            "category",
            "members",
        ]

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation
