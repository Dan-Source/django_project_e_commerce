from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import index, contact
from . import catalog


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contact, name='contact'),
    path('conta/', include('accounts.urls', namespace='accounts')),
    re_path(r'^catalogo/',include('catalog.urls', namespace='catalog')),
    re_path(r'^compras/', include('checkout.urls', namespace='checkout')),
    path('admin/', admin.site.urls),
    path('retorno/pagseguro/', include('pagseguro.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

