from django.db import models

class Unit(models.Model):
    image = models.ImageField(default='media/default_image.jpeg')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
# Create your models here.
