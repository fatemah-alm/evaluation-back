import uuid
from django.db import models
from semesters.models import Project
# Create your models here.
class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="evaluation")
    isLocked = models.BooleanField(default=False)
