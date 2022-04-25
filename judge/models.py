from django.db import models
from semesters.models import Project
from evalutaion.models import Evaluation
import uuid
# Create your models here.
class Judge(models.Model):
    name = models.CharField(max_length=120)
    project =  models.ForeignKey(Project,related_name='judge', on_delete=models.CASCADE)
    grade=models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    

    
# Create your models here.
