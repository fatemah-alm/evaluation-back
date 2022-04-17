from django.db import models
from django.contrib.auth.models import User
from projects.models import Project
# Create your models here.

class Semester(models.Model):
    name = models.CharField(max_length=120)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # projects = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
