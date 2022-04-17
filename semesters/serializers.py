from dataclasses import fields
from rest_framework import serializers
from .models import Semester
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        

class SemesterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'