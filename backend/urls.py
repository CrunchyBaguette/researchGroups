"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from itertools import chain
from rest_framework.routers import DefaultRouter
from backend.users.views import UserViewSet, logout_view, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .research_groups.urls import urlpatterns as research_groups_urls

router = DefaultRouter()
router.register("user", UserViewSet)

api_urlpatterns = list(chain.from_iterable([research_groups_urls]))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("api-auth/", include("rest_framework.urls")),
    path("api/logout/", logout_view, name="logout_view"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
