from django.db import models
from django.contrib.auth.models import User
from backend.tutorials.models import Tutorial
from backend.common.models import Link


# Create your models here.


class ResearchGroup(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    about_us = models.TextField(null=False, blank=False)
    what_we_do = models.TextField(null=False, blank=True)
    contact = models.TextField(null=False, blank=True)
    members = models.ManyToManyField(User, through="ResearchGroupUser", related_name="members")
    guides = models.ManyToManyField(Tutorial, through="ResearchGroupGuide")
    group_owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="group_owner", default=None)

    class Category(models.TextChoices):
        MATH = "math", "Matematyka"
        MEDICAL = "med", "Medycyna"
        CHEMISTRY = "chem", "Chemia"
        DEFAULT = "def", "Default"

    category = models.CharField(max_length=20, choices=Category.choices, default=Category.DEFAULT)


class ResearchGroupUser(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Roles(models.TextChoices):
        MEMBER = "mem", "Member"
        MODERATOR = "mod", "Moderator"
        CREATOR = "cr", "Creator"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.MEMBER)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class ResearchGroupGuide(models.Model):
    is_public = models.BooleanField(default=False)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    guide = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="research_group_guide")


class ResearchGroupPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)


class ResearchGroupPostComment(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(ResearchGroupPost, on_delete=models.CASCADE)


class ResearchGroupDisk(Link):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)


class ResearchGroupLink(Link):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
