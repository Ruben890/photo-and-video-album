# Generated by Django 4.1 on 2022-10-31 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0005_rename_image_galery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, max_length=150, null=True, upload_to='img')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, max_length=150, null=True, upload_to='video')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.DeleteModel(
            name='Galery',
        ),
    ]
