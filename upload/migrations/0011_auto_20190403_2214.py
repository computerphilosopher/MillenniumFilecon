# Generated by Django 2.2 on 2019-04-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_auto_20190403_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='title',
            field=models.TextField(default='', null=True),
        ),
    ]
