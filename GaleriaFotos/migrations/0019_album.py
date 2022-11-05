# Generated by Django 4.1 on 2022-10-31 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0018_delete_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='album of images', max_length=150)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GaleriaFotos.image')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GaleriaFotos.video')),
            ],
            options={
                'ordering': ['name', 'fecha'],
            },
        ),
    ]
