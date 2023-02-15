from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images')
    description = models.TextField()