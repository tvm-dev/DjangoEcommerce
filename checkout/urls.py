from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'checkout'


urlpatterns = [
    path('carrinho/adicionar/<slug>', views.create_cartitem,
    name='create_cartitem'),

]