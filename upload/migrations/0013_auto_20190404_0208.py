# Generated by Django 2.2 on 2019-04-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0012_auto_20190404_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfilemodel',
            name='converted',
            field=models.FileField(default='', upload_to='upload/converted'),
        ),
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.ImageField(upload_to='upload/origin'),
        ),
    ]
