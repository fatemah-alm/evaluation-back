from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Semester
from .serializers import SemesterListSerializer, SemesterDetailSerializer
# Create your views here.

class SemesterListView(ListCreateAPIView):
        queryset = Semester.objects.all()
        serializer_class = SemesterListSerializer

class SemesterDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterDetailSerializer
    lookup_field = 'id'
    

    
