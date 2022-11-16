from django.urls import include, path
from rest_framework import routers

from .views import ResearchGroupViewSet

router = routers.DefaultRouter()

router.register("research-group", ResearchGroupViewSet)

urlpatterns = router.urls
