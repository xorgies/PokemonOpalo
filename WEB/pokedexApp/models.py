from django.db import models

# Create your models here.

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    genderRate = models.CharField(max_length=50)
    growthRate = models.CharField(max_length=50)
    rareness = models.IntegerField()
    happiness = models.IntegerField()
    compatibility = models.CharField(max_length=50)
    stepsToHatch = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    color = models.CharField(max_length=50)
    pokedex = models.TextField()

    
    
    