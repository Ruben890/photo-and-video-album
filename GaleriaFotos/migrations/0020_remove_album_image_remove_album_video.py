# Generated by Django 4.1 on 2022-11-05 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0019_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='image',
        ),
        migrations.RemoveField(
            model_name='album',
            name='video',
        ),
    ]
