from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.IntegerField(unique=True)
    # student = models.BooleanField()
    # tutor = models.BooleanField()
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=264, unique=True)
