# Generated by Django 3.2.18 on 2023-05-12 18:35

import django.core.validators
from django.db import migrations, models
import helpers.files


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20230510_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='', validators=[helpers.files.ValidateFileSize(max_file_size=5), django.core.validators.FileExtensionValidator(allowed_extensions=('jpeg', 'png', 'jpg'))]),
        ),
    ]
