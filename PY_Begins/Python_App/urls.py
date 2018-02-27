from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.loginPage, name='loginPage'),
    url(r'^Registration/', views.registerUser, name='Registration'),
    url(r'^home/', views.loginUser, name='login'),
    url(r'^BookSearch/', views.SecondPage, name='SecondPage'),
    url(r'^BookDetails/', views.BookDetails, name='bookDetails'),
    url(r'^AddBook/', views.AddBook, name='AddBook'),
    url(r'^RemoveBook/', views.removeBook, name='RemoveBook'),
    url(r'^UpdateBook/', views.updateBook, name='UpdateBook'),
    url(r'^weather/', views.weatherForecast, name='weatherForecast'),
]