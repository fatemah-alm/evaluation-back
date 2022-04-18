import imp
from django.db import models
from django.contrib.auth.models import User
# from semesters.models import Semester
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    # teams
    def __str__(self):
        return self.name