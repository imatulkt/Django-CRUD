from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    
    calorie = models.CharField(default=0, max_length=100)

    fat = models.CharField(default=0, max_length=100)
