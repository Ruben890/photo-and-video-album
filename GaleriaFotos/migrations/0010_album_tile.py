# Generated by Django 4.1 on 2022-10-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0009_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='tile',
            field=models.CharField(default='albul de imagenes', max_length=150),
        ),
    ]
