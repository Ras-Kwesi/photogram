from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25,unique=True)
    bio = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='articles/',blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15,blank=True)