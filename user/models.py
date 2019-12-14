from django.db import models
from django.contrib.auth.models import AbstractUser
#MyUser 만들기
class User(AbstractUser):
    phone = models.CharField(max_length=15,default="")
    gender = models.CharField(max_length=7,default="")
    age = models.IntegerField(default=0)
    home_address = models.CharField(max_length=200,default="")
    point = models.IntegerField(default=500)
    def __str__(self):
        return self.username
# Create your models here.
