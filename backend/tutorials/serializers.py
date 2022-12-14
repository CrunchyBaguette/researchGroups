from rest_framework import serializers
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer
from backend.tutorials.models import Tutorial, Rating
from backend.utilsx.serializers import QuerySerializerMixin


class TutorialSerializer(serializers.ModelSerializer):
    owner = UserSerializer(partial=True)
    editors = UserSerializer(many=True, partial=True)
    editable = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Tutorial
        fields = "__all__"
        read_only_fields = ["created", "edited", "editable"]


class TutorialEditSerializer(serializers.ModelSerializer):
    def update(self, instance: Tutorial, validated_data):
        editors = validated_data.get("editors", [])
        if not editors:
            editors = instance.editors.all()

        if instance.owner not in editors:
            editors.append(instance.owner.id)
        instance.title = validated_data.get("title", instance.title)
        instance.text = validated_data.get("text", instance.text)
        instance.is_draft = validated_data.get("is_draft", instance.is_draft)
        instance.is_public = validated_data.get("is_public", instance.is_public)
        ids = [o.id for o in editors]
        editors_to_remove = instance.editors.exclude(id__in=ids)
        instance.save()
        for editor in editors:
            instance.editors.add(editor)
        for editor in editors_to_remove:
            instance.editors.remove(editor)

        return instance

    class Meta:
        model = Tutorial
        fields = ["id", "title", "text", "is_draft", "owner", "editors", "is_public"]
        read_only_fields = ["owner", "id"]
        extra_kwargs = {"editors": {"allow_empty": True}}


class RatingTutorialSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELD = ["author"]

    class Meta:
        model = Rating
        fields = "__all__"


class AddEditorsSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.SlugRelatedField(slug_field="email", queryset=User.objects.all())

    class Meta:
        fields = "__all__"
        write_only_fields = ["id", "username", "email"]
