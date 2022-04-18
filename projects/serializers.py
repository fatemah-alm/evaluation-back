from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from semesters.models import Project
# from semesters.models import Team
from teams.models import Team

class ProjectListSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    teams = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'
        
    
       