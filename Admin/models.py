from django.contrib.auth.models import AbstractUser
from django.db import models

class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
 

    def __str__(self):
        return self.username




 