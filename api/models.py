from django.db import models

class Recipes(models.Model):
    name = models.CharField(unique=False, max_length=100)
    instructions = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=500, default= "")

    def __str__(self):
        return self.name
