from rest_framework import serializers
from backend.announcements.models import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = "__all__"

    def get_author_username(self, obj):
        return obj.author.username

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["ann_type"] = instance.get_ann_type_display()
        return representation
