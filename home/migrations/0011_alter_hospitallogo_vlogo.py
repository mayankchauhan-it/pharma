# Generated by Django 3.2.10 on 2024-01-03 11:15

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20240103_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitallogo',
            name='vLogo',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.get_Logo_upload_path),
        ),
    ]
