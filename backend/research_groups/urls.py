from django.urls import include, path
from rest_framework import routers

from .views import (
    ResearchGroupUserViewSet,
    ResearchGroupViewSet,
    ResearchGroupPostViewSet,
    ResearchGroupLinkViewSet,
    ResearchGroupDiskViewSet,
)

router = routers.DefaultRouter()

router.register("research-group-user", ResearchGroupUserViewSet)
router.register("research-group", ResearchGroupViewSet)
router.register("research-group-post", ResearchGroupPostViewSet)
router.register("research-group-link", ResearchGroupLinkViewSet)
router.register("research-group-disk", ResearchGroupDiskViewSet)

urlpatterns = router.urls
