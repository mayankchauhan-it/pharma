# Generated by Django 3.2.10 on 2024-01-02 11:56

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_hospitalmaster_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.get_upload_path),
        ),
    ]
