# Generated by Django 4.1 on 2022-11-05 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0020_remove_album_image_remove_album_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='albums',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GaleriaFotos.album'),
        ),
        migrations.AddField(
            model_name='video',
            name='albums',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GaleriaFotos.album'),
        ),
    ]
