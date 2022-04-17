from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Semester
from .serializers import SemesterListSerializer
# Create your views here.

class SemesterListView(ListCreateAPIView):
        queryset = Semester.objects.all()
        serializer_class = SemesterListSerializer
