from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^Python_App/', include('Python_App.urls')),
    url(r'^admin/', admin.site.urls),
]