from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EvaluationSerializer, EvaluationDetailSerializer
from .models import Evaluation
# Create your views here.

class EvaluationView(ListCreateAPIView):
    queryset= Evaluation.objects.all()
    serializer_class =EvaluationSerializer
    
    
class EvaluationDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Evaluation.objects.all()
    serializer_class =EvaluationDetailSerializer