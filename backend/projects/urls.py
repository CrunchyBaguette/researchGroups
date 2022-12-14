from django.urls import include, path
from rest_framework import routers

from .views import ProjectViewSet, ProjectUserViewSet, ProjectPostViewSet, ProjectLinkViewSet, ProjectDiskViewSet

router = routers.DefaultRouter()

router.register("project-user", ProjectUserViewSet)
router.register("project", ProjectViewSet)
router.register("project-post", ProjectPostViewSet)
router.register("project-link", ProjectLinkViewSet)
router.register("project-disk", ProjectDiskViewSet)

urlpatterns = router.urls
