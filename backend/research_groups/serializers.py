from rest_framework import serializers

from backend.research_groups.models import ResearchGroup

class ResearchGroupSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = ResearchGroup
        fields = [
            "id",
            "name",
            "description",
            "category",
        ]

    def get_category(self,obj):
        return obj.get_category_display()
