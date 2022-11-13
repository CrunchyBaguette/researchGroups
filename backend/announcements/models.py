from django.db import models
from django.contrib.auth.models import User
from ..research_groups.models import ResearchGroup


# Create your models here.
class Advertisements(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    research_group_id = models.ForeignKey(ResearchGroup, on_delete=models.SET_NULL, null=True)
