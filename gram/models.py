from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25,unique=True)
    bio = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='articles/',blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15,blank=True)


class Image(models.Model):
    image = models.CharField(max_length=40)
    caption = models.CharField(max_length=100)
    path = models.ImageField(upload_to='picture/', default=True)
    poster = models.ForeignKey(Profile)
    likes = models.IntegerField()


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    imagekey = models.ForeignKey(Image)
    commentator = models.ForeignKey(Profile)
