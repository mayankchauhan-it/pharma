# Generated by Django 3.2.10 on 2024-01-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20240102_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalimages',
            name='iLoginID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
