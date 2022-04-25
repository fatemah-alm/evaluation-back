from rest_framework import serializers
from .models import Judge


class JudgeListSerializer(serializers.ModelSerializer):
    grade=serializers.ReadOnlyField
    class Meta:
        model = Judge
        fields = '__all__'
        
        
class JudgeCreateSerializers(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()
    class Meta:
        model=Judge
        fields="__all__"

    def create(self, validated_data):
        defCriteria = []
        teams = []
        for criteria in validated_data['project'].criterias.all():
            defCriteria.append({"id":criteria.id, "name":criteria.name, "weight":criteria.weight, "grade":0})

        for team in validated_data['project'].teams.all():
            teams.append({"id":team.id, "name":team.name, "grade":defCriteria})



        validated_data['grade'] = teams
        return super().create(validated_data)

        
class JudgeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'