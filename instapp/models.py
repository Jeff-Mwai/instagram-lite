from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=250, blank=True)
    image_caption = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=250, blank=True)


    @classproperty
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=250, blank=True)

