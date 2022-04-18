import imp
from django.db import models
from django.contrib.auth.models import User
from semesters.models import Project
# Create your models here.


    
class Team(models.Model):
    name = models.CharField(max_length=120)
    project =  models.ForeignKey(Project,related_name='teams', on_delete=models.CASCADE)
        
    def __str__(self):
        return self.name