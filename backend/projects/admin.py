from django.contrib import admin
from .models import (
    Project,
    GuideProject,
    ProjectUser,
    ProjectPost,
    ProjectPostComment,
    ProjectDisk,
    ProjectLink,
)

admin.site.register(Project)
admin.site.register(GuideProject)
admin.site.register(ProjectUser)
admin.site.register(ProjectPost)
admin.site.register(ProjectPostComment)
admin.site.register(ProjectDisk)
admin.site.register(ProjectLink)
# Register your models here.
