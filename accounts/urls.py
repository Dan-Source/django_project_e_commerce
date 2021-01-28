from django.urls import path, re_path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('alterar-dados', views.update_user, name='update_user'),
    path('alterar-senha', views.update_password, name='update_password'),
    path('registro', views.register, name='register'),
]
