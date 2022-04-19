from django.db import models
from semesters.models import Project
# Create your models here.


    
class Team(models.Model):
    name = models.CharField(max_length=120)
    project =  models.ForeignKey(Project,related_name='teams', on_delete=models.CASCADE)
    members = models.CharField(max_length=120, blank=True)
        
    def __str__(self):
        return self.name