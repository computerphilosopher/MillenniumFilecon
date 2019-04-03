from django.db import models

class UploadFileModel(models.Model):
    title = models.TextField(default='', null = True)
    file = models.ImageField(null=False)

    def __str__(self):
        return self.title