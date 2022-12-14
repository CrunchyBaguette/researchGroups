from django.db import models
from django.contrib.auth.models import User
from backend.tutorials.models import Tutorial
from backend.research_groups.models import ResearchGroup
from backend.common.models import Link


# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    contact = models.TextField(null=False, blank=True)
    deadline = models.DateField(null=True, blank=True)
    funds = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    members = models.ManyToManyField(User, through="ProjectUser")
    project_owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="project_owner", default=None)
    guides = models.ManyToManyField(Tutorial, through="GuideProject")
    research_groups = models.ManyToManyField(ResearchGroup, blank=True)

    class Category(models.TextChoices):
        MATH = "math", "Matematyka"
        MEDICAL = "med", "Medycyna"
        CHEMISTRY = "chem", "Chemia"
        DEFAULT = "def", "Default"

    category = models.CharField(max_length=20, choices=Category.choices, default=Category.DEFAULT)


class GuideProject(models.Model):
    is_public = models.BooleanField(default=False)
    guide = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name="project_guide")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)


class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    class Roles(models.TextChoices):
        MEMBER = "mem", "Member"
        MODERATOR = "mod", "Moderator"
        OWNER = "own", "Owner"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.MEMBER)
    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


class ProjectPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectPostComment(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(ProjectPost, on_delete=models.CASCADE)


class ProjectDisk(Link):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectLink(Link):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
