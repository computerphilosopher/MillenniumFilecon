from django.db import models

class Unit(models.Model):
    '''
    filename = models.CharField(max_length=50)
    gif_file = models.FileField(blank = true, upload_to='gif')
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
# Create your models here.
