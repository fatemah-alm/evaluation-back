from rest_framework import serializers
from .models import Criteria
from django.contrib.auth.models import User


class CriteriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'
        
        
class CriteriaDetailSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField(method_name='getProjects')
    class Meta:
        model = Criteria
        fields = '__all__'
        
        
    def getProjects(self,criteria:Criteria):
        projects = []
        for project in criteria.project_set.all():
            projects.append(project.name)
        return projects  
