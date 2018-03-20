from django.contrib import admin

from .models import Book, User, Task

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Task)