from django.urls import path, re_path

from catalog.views import product_list, category, product

app_name = 'catalog'

urlpatterns = [
    re_path(r'^$', product_list, name='product_list'),
    re_path(r'^(?P<slug>[\w_-]+)/$', category, name='category'),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', product, name='product'),
]