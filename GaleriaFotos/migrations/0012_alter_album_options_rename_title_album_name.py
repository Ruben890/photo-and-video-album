# Generated by Django 4.1 on 2022-10-31 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GaleriaFotos', '0011_alter_album_options_rename_tile_album_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name', 'fecha']},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='title',
            new_name='name',
        ),
    ]
