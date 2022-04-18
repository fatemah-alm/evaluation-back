from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from semesters.models import Project

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'