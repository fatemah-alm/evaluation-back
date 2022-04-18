from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Team
from .serializers import TeamsListSerializer,TeamDetailSerializer
# Create your views here.


class TeamsListView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamsListSerializer
    
    
class TeamsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    lookup_field = 'id'