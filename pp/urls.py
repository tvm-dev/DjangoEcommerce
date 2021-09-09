
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.static import serve as serve_static
from core import views
from django.views.static import serve as serve_static
from catalog import views as views_catalog

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]

