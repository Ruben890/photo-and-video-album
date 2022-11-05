# Generated by Django 4.1 on 2022-10-31 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, max_length=250, null=True, upload_to='img')),
                ('video', models.FileField(blank=True, max_length=150, null=True, upload_to='video')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
    ]
