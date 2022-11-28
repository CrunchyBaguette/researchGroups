from django.urls import include, path
from rest_framework import routers

from .views import AnnouncementViewSet

router = routers.DefaultRouter()

router.register("announcement", AnnouncementViewSet)

urlpatterns = router.urls
