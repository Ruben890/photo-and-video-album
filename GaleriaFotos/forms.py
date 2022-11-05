from django import forms
from .models import Image, Video


class ImangeForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

    img = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))


class VideosForms(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        
    video = forms.FileField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-contorl'}))

