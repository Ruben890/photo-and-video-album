from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Image, Video, Album
from .forms import ImangeForm, VideosForms


def HomePage(request):
    contents = {
        'img': Image.objects.all(),
        'video': Video.objects.all()
    }

    return render(request, 'index.html', contents)


# ?eliminar imagenes
def EliminarImages(request, id):
    img = Image.objects.get(id=id)
    img.delete()
    return redirect('HomePage')


# ?eliminiar videos
def Eliminarvideo(request, id):
    video = Video.objects.get(id=id)
    video.delete()
    return redirect('HomePage')


class DetailGalery(DetailView):
    model = Image
    template_name = 'DetailGalery.html'
    context_object_name = 'gal'


class ImportGalery(View):
    def get(self, request):
        img = ImangeForm
        video = VideosForms
        contents = {
            'img': img,
            'video': video
        }
        return render(request, 'CargarImg.html', contents)

    def post(self, request):
        video = VideosForms(request.POST, request.FILES)
        img = ImangeForm(request.POST, request.FILES)

        if img.is_valid() and video.is_valid():
            img.save()
            video.save()
            return redirect('HomePage')


class albums(ListView):
    model = Album
    template_name = 'Albums.html'
    context_object_name = 'album'
    
"""
If someone knows how to create a new album or using the images that are already in the database, let me know. please😅😅😅

"""
#
#class CreateAbums(CreateView):
 #   model = Album
  #  template_name = "agregarAlbum.html"
   # fields = '__all__'
    #success_url = reverse_lazy('HomePage')

 #   def form_valid(self, form):
  #      form.instance.Image = self.request.Image
   #     form.instance.Video = self.request.Video
    #    return super(Image, Video, self).form_valid(form)
        
