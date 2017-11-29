from django.db import models

class Book(models.Model):
    Book_id = models.CharField(max_length=10, primary_key=True)
    Name = models.CharField(max_length=200)
    Publication = models.CharField(max_length=200)

