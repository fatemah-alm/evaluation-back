from rest_framework import serializers
from .models import Semester, Project
from django.contrib.auth.models import User
from projects.serializers import ProjectListSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        

class SemesterListSerializer(serializers.ModelSerializer):
    project_set = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Semester
        fields = '__all__'
  
        
        
class SemesterDetailSerializer(serializers.ModelSerializer):
    project_set = ProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Semester
        fields = '__all__'
        
   
    
    
