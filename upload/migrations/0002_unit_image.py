# Generated by Django 2.2 on 2019-04-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='image',
            field=models.ImageField(default='media/default_image.jpeg', upload_to=''),
        ),
    ]
