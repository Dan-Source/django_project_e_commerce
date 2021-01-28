"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
<<<<<<< HEAD
from core.views import index, contact
from django.contrib.auth import login, logout
=======
from core.views import index, contact, register
>>>>>>> test_login_cadastro
from . import catalog


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
    path('entrar/', login, name='login'),
    path('sair/', logout, name='logout'),
=======
    path('registro/', register, name='register'),
>>>>>>> test_login_cadastro
    re_path(r'^catalogo/',include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]
