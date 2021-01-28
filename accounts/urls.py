from django.urls import path, re_path

from . import views 

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.register, name='register'),
]
