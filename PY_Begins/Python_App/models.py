from django.db import models

class Book(models.Model):
    Book_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Publication = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)

