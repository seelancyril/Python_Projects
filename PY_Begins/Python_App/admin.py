from django.contrib import admin

from .models import Book, User

admin.site.register(Book)
admin.site.register(User)