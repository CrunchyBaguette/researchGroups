from django.urls import include, path
from rest_framework import routers

from .views import ProjectViewSet, ProjectUserViewSet, ProjectPostViewSet

router = routers.DefaultRouter()

router.register("project-user", ProjectUserViewSet)
router.register("project", ProjectViewSet)
router.register("project-post", ProjectPostViewSet)

urlpatterns = router.urls
