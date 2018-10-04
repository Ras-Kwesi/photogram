from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=25)
    username = models.CharField(max_length=25,unique=True)
    bio = models.CharField(max_length=100)
    profilepic = models.ImageField(upload_to='articles/',blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']

    def save_profile(self):
        self.save()



class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commentator = models.ForeignKey(Profile)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()





class Image(models.Model):
    image = models.CharField(max_length=40)
    caption = models.CharField(max_length=100)
    path = models.ImageField(upload_to='picture/', default=True)
    poster = models.ForeignKey(Profile)
    likes = models.IntegerField()
    imagecomments = models.ForeignKey(Comment)
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image(cls,id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def getImages(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def image_comments(cls,id):
        comments = cls.objects.filter(imagecomments__comment_id=id)
        posters = cls.objects.filter(imagecomments__commnetator__id=id)