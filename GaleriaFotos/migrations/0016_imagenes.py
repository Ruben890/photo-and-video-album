# Generated by Django 4.1 on 2022-10-31 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0015_alter_album_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
                ('imagenes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GaleriaFotos.image')),
            ],
        ),
    ]
