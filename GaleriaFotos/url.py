from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name="HomePage"),
    path('DetailGalery/<int:pk>', DetailGalery.as_view(), name='DetailGalery'),
    path('ImportGalery', ImportGalery.as_view(), name="ImportGalery"),
    path('EliminarImagenes/<int:id>', EliminarImages, name='EliminarImagenes'),
    path('Eliminarvideo/<int:id>', Eliminarvideo, name='Eliminarvideo'),
    path('Album', albums.as_view(), name='Album'),
    path('CreateAbums', CreateAbums.as_view(), name='CreateAbums')


]
