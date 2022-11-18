from django.shortcuts import render
from rest_framework import viewsets
from backend.research_groups.serializers import ResearchGroupSerializer
from backend.research_groups.models import ResearchGroup

# Create your views here.
class ResearchGroupViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroup.objects.all()
    serializer_class = ResearchGroupSerializer