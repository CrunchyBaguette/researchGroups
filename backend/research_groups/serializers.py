from rest_framework import serializers

from backend.research_groups.models import ResearchGroup

class ResearchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroup
        fields = [
            "name",
            "description",
        ]
