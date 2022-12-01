from django.db import models
from django.contrib.auth.models import User
from backend.research_groups.models import ResearchGroup


# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    research_group_id = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True)

    class Type(models.TextChoices):
        SPONSOR = "sponsor", "Poszukiwanie sponsora"
        RECRUITMENT = "rekrutacja", "Poszukiwanie nowych członków"
        PROJECT = "projekt", "Poszukiwanie osób do projektu"
        DEFAULT = "def", "Default"

    ann_type = models.CharField(max_length=30, choices=Type.choices, default=Type.DEFAULT)
