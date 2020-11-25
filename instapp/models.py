from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    @classmethod
    def search_by_name(cls, search_term):
        userProfile = cls.objects.filter(user__username__icontains=search_term).all()
        return userProfile

class Image(models.Model):
    image = CloudinaryField('image')
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

    

class Comment(models.Model):
    post = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='commentss')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f'{self.post.profile}, {self.user.username}'

    class Meta:
        db_table = 'comment'

    def save_comment(self):
        self.save()


