from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Criteria
from .serializers import CriteriaListSerializer, CriteriaDetailSerializer
# Create your views here.


class CriteriaListView(ListCreateAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaListSerializer
    
    
class CriteriaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaDetailSerializer
    lookup_field = 'id'
    
    
    
