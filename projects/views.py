from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from semesters.models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
# Create your views here.

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    lookup_field = 'id'

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.prefetch_related('teams')
    serializer_class = ProjectDetailSerializer
    lookup_field = 'id'