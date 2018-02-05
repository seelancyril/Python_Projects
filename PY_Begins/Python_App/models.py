from django.db import models

class Book(models.Model):
    Book_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Publication = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)

class User(models.Model):
    UID = models.CharField(primary_key=True, max_length=50)
    User_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Role = models.CharField(max_length=20)
    logged_In = models.CharField(max_length=100)

