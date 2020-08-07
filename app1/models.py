from django.db import models
from django.contrib.auth.models import User

class Student_registartion(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

class Add_class(models.Model):
    fno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.IntegerField()
    #class Meta:
     #   db_table = "add_clss"