from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile_picture = models.ImageField(upload_to='images/', default='image.jpg')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=250)
    image_caption = models.CharField(max_length=250)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()


    def delete_image(cls, self):
        self.delete()

    def update_caption(cls, self):
        self.update()

    




