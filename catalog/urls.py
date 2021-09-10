#tvm: In this file, we have only Urls from Catalog aplicattion
app_name = 'catalog'

from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
      path(r'', views.product_list, name='product_list'),
      path('<slug>/', views.category, name='category'), #mode tvm2
      path('produtos/<slug>/', views.product, name='product'),
 ]