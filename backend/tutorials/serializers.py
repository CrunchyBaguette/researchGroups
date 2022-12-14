from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from django.contrib.auth.models import User
from backend.users.serializers import UserSerializer
from backend.tutorials.models import Tutorial, Rating
from backend.research_groups.models import ResearchGroupGuide
from backend.projects.models import GuideProject
from backend.utilsx.serializers import QuerySerializerMixin


class TutorialSerializer(serializers.ModelSerializer):
    owner = UserSerializer(partial=True)
    editors = UserSerializer(many=True, partial=True)
    editable = serializers.BooleanField(read_only=True, default=False)
    category_code = serializers.SerializerMethodField()

    class Meta:
        model = Tutorial
        fields = "__all__"
        read_only_fields = ["created", "edited", "editable"]

    def get_category_code(self, obj):
        return obj.category

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = instance.get_category_display()
        return representation


class TutorialEditSerializer(serializers.ModelSerializer):

    editor_emails = serializers.ListField(allow_null=False, default=[], child=serializers.EmailField(), write_only=True)

    def create(self, validated_data):
        data = validated_data
        editor_emails = data.get("editor_emails", [])
        if editor_emails:
            editors = User.objects.filter(email__in=editor_emails).all()
            serializer = UserSerializer(editors, many=True)
            data["editors"] = serializer.data

        del data["editor_emails"]

        return super().create(data)

    def update(self, instance: Tutorial, validated_data):
        raise_errors_on_nested_writes("update", self, validated_data)
        editors = validated_data.get("editors", [])
        editor_emails = validated_data.get("editor_emails", [])
        if not editors and not editor_emails:
            editors = instance.editors.all()
            if instance.owner not in editors:
                editors.append(instance.owner)
        elif editor_emails:
            if instance.owner.email not in editor_emails:
                editor_emails.append(instance.owner.email)
            users = User.objects.filter(email__in=editor_emails)
            editors = users
        elif instance.owner not in editors:
            editors.append(instance.owner)

        instance.title = validated_data.get("title", instance.title)
        instance.text = validated_data.get("text", instance.text)
        instance.is_draft = validated_data.get("is_draft", instance.is_draft)
        instance.is_public = validated_data.get("is_public", instance.is_public)
        instance.category = validated_data.get("category", instance.category)
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
        fields = ["id", "category", "title", "text", "is_draft", "owner", "editors", "is_public", "editor_emails"]
        read_only_fields = ["owner", "id"]
        extra_kwargs = {"editors": {"allow_empty": True, "allow_null": True}}


class RatingTutorialSerializer(QuerySerializerMixin, serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    RELATED_FIELD = ["author"]

    class Meta:
        model = Rating
        fields = "__all__"


class TutorialLinkProject(serializers.ModelSerializer):
    class Meta:
        model = GuideProject
        fields = "__all__"
        extra_kwargs = {"is_public": {"required": False}, "added": {"required": False, "read_only": True}}


class TutorialLinkResearchGroup(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroupGuide
        fields = "__all__"
        extra_kwargs = {"is_public": {"required": False}}
