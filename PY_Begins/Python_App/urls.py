from django.conf.urls import url

from . import views, taskAssigner

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
    url(r'^task/edit/', taskAssigner.editTask, name='editTask'),
    url(r'^task/delete/', taskAssigner.deleteTask, name='deleteTask'),
    url(r'^task/', views.taskAssigner, name='taskAssigner'),
    url(r'^create_task/', taskAssigner.create_task, name='create_task'),
    url(r'^logout/', views.logoutUser, name='logoutUser'),
]