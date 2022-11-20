from django.shortcuts import render
from rest_framework import viewsets
from backend.research_groups.serializers import ResearchGroupSerializer
from backend.research_groups.models import ResearchGroup
from django.contrib.auth.models import User

# Create your views here.
class ResearchGroupViewSet(viewsets.ModelViewSet):
    queryset = ResearchGroup.objects.all()
    serializer_class = ResearchGroupSerializer

    def create(self, request, *args, **kwargs):
        # Obecnie, w przypadku gdy nie ma użytkownika z podanym mailem, tworzony jest
        # nowy ale później można tu zaimplementować rozsyłanie maili
        members = request.data["members"]
        for member in members:
            if not User.objects.filter(email=member).exists():
                User.objects.create_user(
                    username=member.split("@")[0],
                    password=member.split("@")[0],
                    email=member,
                )
        return super().create(request, *args, **kwargs)
