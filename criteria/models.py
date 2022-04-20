from django.db import models
# Create your models here.


    

# Create your models here.


class Criteria(models.Model):
    name = models.CharField(max_length=120)
    weight = models.IntegerField()
    def __str__(self):
        return self.name
    
    
    
