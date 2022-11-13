from django.db import models
from ..tutorials.models import Tutorial
from ..research_groups.models import ResearchGroup
from django.contrib.auth.models import User


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True)
    funds = models.DecimalField(decimal_places=2, max_digits=20)
    guides = models.ManyToManyField(Tutorial, through="GuideProject")
    research_groups = models.ManyToManyField(ResearchGroup)

    class Category(models.TextChoices):
        DEFAULT = "def", "Default"

    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.DEFAULT
    )


class GuideProject(models.Model):
    is_public = models.BooleanField(default=False)
    guide = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)


class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Roles(models.TextChoices):
        UNSPECIFIED = "un", "Unspecified"
        MEMBER = "mem", "Member"
        MODERATOR = "mod", "Moderator"
        OWNER = "own", "Owner"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.UNSPECIFIED
    )
    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
