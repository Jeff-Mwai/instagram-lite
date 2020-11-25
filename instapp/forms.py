from django import forms
from django.contrib.auth.models import User
from .models import Profile, Image, Comment
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'image_caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_picture', 'bio']

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user 