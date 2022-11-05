from django.db import models


# ? album de imagenes
class Album(models.Model):
    name = models.CharField(max_length=150, default="album of images")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'fecha']


class Image(models.Model):
    albums = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(
        max_length=150, upload_to='img', null=True, blank=True)

    fecha = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['fecha']


class Video(models.Model):
    albums = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(max_length=150,
                             upload_to='video', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha']
