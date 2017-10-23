from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.IntegerField(unique=True)
    student = models.BooleanField()
    tutor = models.BooleanField()
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=264, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class Tutor(models.Model):
    id = models.IntegerField(unique=True)
    user = models.ForeignKey(User)
    rating = models.IntegerField()
    hourly_rate = models.IntegerField()

class TutorSchedule(models.Model):
    tutor = models.ForeignKey(Tutor)
    date = models.DateField()
    time = models.DateTimeField()

class Session(models.Model):
    is_booked = models.BooleanField()
    is_free = models.BooleanField()
    is_running = models.BooleanField()
    is_booked_cant_cancel = models.BooleanField()
    tutor = models.ForeignKey(Tutor)

class Student(models.Model):
    user = models.ForeignKey(User)
    university = models.CharField(user)
