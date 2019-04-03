from django.db import models

class UploadFileModel(models.Model):
    title = models.TextField(default='', null = True)
    file = models.FileField(null=False)