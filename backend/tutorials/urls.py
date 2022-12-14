from rest_framework import routers
from backend.tutorials.views import TutorialViewSet

router = routers.DefaultRouter()

router.register("tutorial", TutorialViewSet)

urlpatterns = router.urls
