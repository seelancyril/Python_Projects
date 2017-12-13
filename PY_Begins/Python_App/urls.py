from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Second_Page/', views.SecondPage, name='SecondPage'),
    url(r'^BookDetails/', views.BookDetails, name='bookDetails'),
]