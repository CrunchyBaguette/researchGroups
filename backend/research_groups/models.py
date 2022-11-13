from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ResearchGroup(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(null=False)
    about_us = models.TextField(null=False)
    what_we_do = models.TextField(null=False)
    contact = models.TextField(null=False)
    members = models.ManyToManyField(User, through="ResearchGroupsUsers")

    class Categories(models.TextChoices):
        MATH = "math", "Math"
        MEDICAL = "med", "Medical"
        CHEMISTRY = "chem", "Chemistry"
        DEFAULT = "def", "Default"

    category = models.CharField(
        max_length=20, choices=Categories, default=Categories.DEFAULT
    )


class ResearchGroupsUsers(models.Model):
    research_group = models.ForeignKey(ResearchGroup, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Roles(models.TextChoices):
        UNSPECIFIED = "un", "Unspecified"
        MEMBER = "mem", "Member"
        MODERATOR = "mod", "Moderator"

    role = models.CharField(max_length=20, choices=Roles, default=Roles.UNSPECIFIED)
    added = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
