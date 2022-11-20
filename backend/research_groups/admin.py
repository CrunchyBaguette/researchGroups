from django.contrib import admin
from .models import ResearchGroup, ResearchGroupUser, ResearchGroupGuide, ResearchGroupPost, ResearchGroupPostComment, ResearchGroupDisk, ResearchGroupLink

admin.site.register(ResearchGroup)
admin.site.register(ResearchGroupUser)
admin.site.register(ResearchGroupGuide)
admin.site.register(ResearchGroupPost)
admin.site.register(ResearchGroupPostComment)
admin.site.register(ResearchGroupDisk)
admin.site.register(ResearchGroupLink)
# Register your models here.
