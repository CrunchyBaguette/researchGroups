from django.db import models


# Create your models here.
class Link(models.Model):
    link = models.URLField()
    is_public = models.BooleanField(default=False)

    class Meta:
        abstract = True
