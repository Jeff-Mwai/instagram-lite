from django import forms
from django.contrib.auth.models import User
from .models import Profile, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_caption')