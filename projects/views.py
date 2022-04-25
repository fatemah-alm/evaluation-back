from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS
from semesters.models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
# Create your views here.

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    def get_serializer_class(self):
        if(self.request.method in SAFE_METHODS):
            return ProjectDetailSerializer
        else:
            return ProjectListSerializer
    
   

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    lookup_field = 'id'