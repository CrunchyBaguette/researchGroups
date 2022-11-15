from django.db import models
from django.contrib.auth.models import User
from backend.research_groups.models import ResearchGroup


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    research_group_id = models.ForeignKey(
        ResearchGroup, on_delete=models.SET_NULL, null=True
    )
    is_public = models.BooleanField(default=False)

    class Type(models.TextChoices):
        DEFAULT = "def", "Default"

    ann_type = models.CharField(max_length=20, choices=Type.choices)