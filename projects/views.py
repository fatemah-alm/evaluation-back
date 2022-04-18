from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from semesters.models import Project
from .serializers import ProjectListSerializer
# Create your views here.

class ProjectListView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    lookup_field = 'id'
