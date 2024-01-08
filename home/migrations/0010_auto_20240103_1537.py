# Generated by Django 3.2.10 on 2024-01-03 10:07

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_hospitalimages_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitallogo',
            name='iLoginID',
        ),
        migrations.RemoveField(
            model_name='hospitallogo',
            name='vLogoID',
        ),
        migrations.AddField(
            model_name='hospitallogo',
            name='vLogo',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.get_upload_path),
        ),
    ]