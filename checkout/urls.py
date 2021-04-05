from django.urls import re_path, include

from . import views

app_name = 'checkout'

urlpatterns = [
    re_path(
        r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', 
        views.create_cartitem,
        name='create_cartitem'
    ),
    re_path(r'^carrinho/$', views.cart_item, name='cart_item'),
    re_path(r'^finalizando/$', views.checkout, name='checkout'),
    re_path(
        r'^finalizando/(?P<pk>\d+)/pagseguro/$', views.pagseguro_view,
        name='pagseguro_view'
    ),
    #re_path(r'^retorno/pagseguro/', include('pagseguro.urls')),
    re_path(r'^meus-pedidos/$', views.order_list, name='order_list'),
    re_path(
        r'^meus-pedidos/(?P<pk>\d+)/$', 
        views.order_detail, name='order_detail'
    ),
    re_path(
        r'^notificacoes/pagseguro/$', views.pagseguro_notification,
        name='pagseguro_notification'
    ),
]