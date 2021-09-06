#tvm: In this file, we have only Urls from Catalog aplicattion
app_name = 'catalog'

from django.conf.urls import url
from .views import Product
from . import views
from django.urls import path

urlpatterns = [
      path(r'', views.product_list, name='product_list'),
      path(r'(?P<slug>[\w_-]+)/', views.category, name='category'), #mode tvm
      #path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'), #mode video
 ]