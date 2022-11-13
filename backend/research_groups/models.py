from django.db import models
from django.contrib.auth.models import User
from ..tutorials.models import Guide

# Create your models here.


class ResearchGroup(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    about_us = models.TextField(null=False, blank=True)
    what_we_do = models.TextField(null=False, blank=True)
    contact = models.TextField(null=False, blank=True)
    members = models.ManyToManyField(User, through="ResearchGroupUser")
    guides = models.ManyToManyField(Guide, through="ResearchGroupGuide")

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

    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.UNSPECIFIED
    )
    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class ResearchGroupGuide(models.Model):
    is_public = models.BooleanField(default=False)
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
