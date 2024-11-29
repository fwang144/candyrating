from django.db import models

# Create your models here.
class Candy(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    rating = models.IntegerField(null=True)
    
    
