from django.contrib import admin
from .models import Image, Video, Album


@admin.register(Image)
class Admin(admin.ModelAdmin):
    list_display = ('fecha',)


@admin.register(Video)
class Admin(admin.ModelAdmin):
    list_display = ('fecha',)


@admin.register(Album)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'fecha']
