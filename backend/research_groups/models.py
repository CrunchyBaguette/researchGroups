from django.db import models
from django.contrib.auth.models import User
from backend.tutorials.models import Tutorial
from backend.common.models import Link


# Create your models here.


class ResearchGroup(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    about_us = models.TextField(null=False, blank=True)
    what_we_do = models.TextField(null=False, blank=True)
    contact = models.TextField(null=False, blank=True)
    members = models.ManyToManyField(User, through="ResearchGroupUser")
    guides = models.ManyToManyField(Tutorial, through="ResearchGroupGuide")

    class Category(models.TextChoices):
        MATH = "math", "Math"
        MEDICAL = "med", "Medical"
        CHEMISTRY = "chem", "Chemistry"
        DEFAULT = "def", "Default"

    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.DEFAULT
    )


class ResearchGroupUser(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Roles(models.TextChoices):
        UNSPECIFIED = "un", "Unspecified"
        MEMBER = "mem", "Member"
        MODERATOR = "mod", "Moderator"
        CREATOR = "cr", "Creator"

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.UNSPECIFIED
    )
    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class ResearchGroupGuide(models.Model):
    is_public = models.BooleanField(default=False)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    guide = models.ForeignKey(Tutorial, on_delete=models.CASCADE)


class ResearchGroupPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True)
    added = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now_add=True)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)


class ResearchGroupPostComment(models.Model):
    test = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(ResearchGroupPost, on_delete=models.CASCADE)


class ProjectDisk(Link):
    project = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)


class ProjectLink(Link):
    project = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
