from rest_framework import serializers
from .models import Criteria
from django.contrib.auth.models import User


class CriteriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'
        
        
class CriteriaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Criteria
        fields = '__all__'