from django.db import models

class Image(models.Model):
    image = models.ImageField(default='media/default_image.jpeg')
    gif_name = models.CharField(max_length=30, default = " ")
    
# Create your models here.
