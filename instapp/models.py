from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=250, blank=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=250, blank=True)
    image_caption = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=250, blank=True)


    @classmethod
    def save_image(cls, self):
        self.save()

    def delete_image(cls, self):
        self.delete()

    def update_caption(cls, self):
        self.update()



