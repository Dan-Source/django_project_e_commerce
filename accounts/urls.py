from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('registro', views.register, name='register'),
    path('entrar/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
    ]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
