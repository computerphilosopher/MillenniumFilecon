from django.db import models

class UploadFileModel(models.Model):
    title = models.TextField(default='', null = True)
    file = models.ImageField(upload_to='upload/origin', null=False)
    converted = models.FileField(upload_to='upload/converted', null = False,default='')

    def __str__(self):
        return self.title