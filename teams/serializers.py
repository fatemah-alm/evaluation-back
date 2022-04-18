from rest_framework import serializers
from semesters.models import Project
from .models import Team
from django.contrib.auth.models import User


class TeamsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
        
class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'