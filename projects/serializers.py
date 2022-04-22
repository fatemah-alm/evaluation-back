from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from semesters.models import Project
from teams.serializers import TeamsListSerializer
from criteria.serializers import CriteriaListSerializer
# from semesters.serializers import SemesterListSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    teams = TeamsListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        
        
  
        
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    teams = TeamsListSerializer(many=True, read_only=True)
    criterias = CriteriaListSerializer(many=True, read_only=True)
    # semester = SemesterListSerializer(read_only=True)


    class Meta:
        model = Project
        fields = '__all__'
        
 
        
   
        
    
       