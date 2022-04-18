from dataclasses import fields
from rest_framework import serializers
from .models import Semester, Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        

class SemesterListSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField(method_name='getProjects')

    class Meta:
        model = Semester
        fields = '__all__'
    def getProjects(self,project:Project):
        semester = []
        for project in project.project_set.all():
            semester.append(project.name)
        return semester
        
        
class SemesterDetailSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField(method_name='getProjects')
    class Meta:
        model = Semester
        fields = '__all__'
        
    def getProjects(self,project:Project):
        semester = []
        for project in project.project_set.all():
            semester.append(project.name)
        return semester
    
    
