from django.urls import path, re_path

from . import views 

app_name = 'accounts'
urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('conta/', include('accounts.urls')),
    re_path(r'^catalogo/',include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]
