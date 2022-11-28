from django.urls import include, path
from rest_framework import routers

from .views import (
    ResearchGroupUserViewSet,
    ResearchGroupViewSet,
    ResearchGroupPostViewSet,
)

router = routers.DefaultRouter()

router.register("research-group-user", ResearchGroupUserViewSet)
router.register("research-group", ResearchGroupViewSet)
router.register("research-group-post", ResearchGroupPostViewSet)

urlpatterns = router.urls
