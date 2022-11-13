from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Guide(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField(null=False, blank=True)
    is_draft = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    editors = models.ManyToManyField(User)

    class Types(models.TextChoices):
        DEFAULT = "def", "Default"

    type = models.CharField(max_length=20, choices=Types.choices, default=Types.DEFAULT)


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=False)

    class Marks(models.IntegerChoices):
        GREAT = 5
        GOOD = 4
        DECENT = 3
        OK = 2
        BAD = 1

    mark = models.IntegerField(choices=Marks.choices, null=False)
