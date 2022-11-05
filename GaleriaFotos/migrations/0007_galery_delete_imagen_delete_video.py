# Generated by Django 4.1 on 2022-10-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0006_imagen_video_delete_galery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, max_length=150, null=True, upload_to='img')),
                ('video', models.FileField(blank=True, max_length=150, null=True, upload_to='video')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]