from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=30, blank=True)
    is_public = models.BooleanField(default=False)
    users = models.ManyToManyField(User, blank=True)

    class Meta:
        abstract = True
