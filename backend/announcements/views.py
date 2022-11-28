from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from backend.announcements.models import Announcement
from backend.announcements.serializers import AnnouncementSerializer


class StandardPagination(PageNumberPagination):
    page_size = 5


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    pagination_class = StandardPagination
    serializer_class = AnnouncementSerializer
