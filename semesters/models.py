from django.db import models
from django.contrib.auth.models import User
from criteria.models import Criteria




class Semester(models.Model):
    name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # projects = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=120)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True)
    criterias = models.ManyToManyField(Criteria)
    

    def __str__(self):
        return self.name
    
    
