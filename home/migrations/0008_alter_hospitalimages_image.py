# Generated by Django 3.2.10 on 2024-01-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_hospitalimages_iloginid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
