from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(AbstractUser):
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    class Meta:
        managed=True
        db_table='user_profile'
    def __str__(self):
        return self.first_name + ' _ ' + self.last_name
        # return self.user.username


class Post_Catagory(models.Model):
    catagory_name = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    catagory = models.ForeignKey(Post_Catagory, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.TimeField(max_length=50)

    def __str__(self):
        return self.title

class Post_Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.description
