from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Judge
from .serializers import JudgeListSerializer,JudgeCreateSerializers,JudgeDetailSerializer
# Create your views here.


class JudgeListView(ListCreateAPIView):
    queryset = Judge.objects.all()

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return JudgeCreateSerializers
        return JudgeListSerializer    
    
class JudgeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Judge.objects.all()
    serializer_class = JudgeDetailSerializer
    lookup_field = 'id'