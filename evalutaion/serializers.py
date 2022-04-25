from dataclasses import field
from rest_framework import serializers
from .models import Evaluation
from judge.serializers import JudgeListSerializer

class EvaluationSerializer(serializers.ModelSerializer):
    judge = JudgeListSerializer(many=True, read_only=True)

    class Meta:
        model= Evaluation
        fields = '__all__'
        
        


class EvaluationDetailSerializer(serializers.ModelSerializer):
    judge = JudgeListSerializer(many=True, read_only=True)

    class Meta:
        model= Evaluation
        fields = '__all__'
        