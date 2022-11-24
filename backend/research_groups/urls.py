from django.urls import include, path
from rest_framework import routers

from .views import ResearchGroupViewSet, GroupForumPostViewSet

router = routers.DefaultRouter()

router.register("research-group", ResearchGroupViewSet)
router.register("group-forum-post", GroupForumPostViewSet)

urlpatterns = router.urls
