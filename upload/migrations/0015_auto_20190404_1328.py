# Generated by Django 2.2 on 2019-04-04 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0014_uploadfilemodel_uri_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfilemodel',
            old_name='uri_path',
            new_name='converted_url',
        ),
    ]
