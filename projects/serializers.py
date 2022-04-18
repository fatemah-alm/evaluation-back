from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from semesters.models import Project
from teams.serializers import TeamsListSerializer

class ProjectListSerializer(serializers.ModelSerializer):
    teams = TeamsListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    teams = TeamsListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        
    
       