from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'checkout'


urlpatterns = [
    path('carrinho/adicionar/<slug:slug>/', views.create_cartitem, name='create_cartitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    path('meus-pedidos/', views.order_list, name='order_list'),
    path('meus-pedidos/<pk>', views.order_detail, name='order_detail'),
   
]


