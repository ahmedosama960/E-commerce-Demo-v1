from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.

class User(AbstractUser):
    phone=models.CharField(max_length=14,null=True,blank=True)