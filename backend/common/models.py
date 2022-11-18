from django.db import models


# Create your models here.
class Link(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=30, blank=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        abstract = True
