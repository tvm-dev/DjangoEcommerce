
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.static import serve as serve_static
from core import views
from django.views.static import serve as serve_static
from catalog import views as views_catalog
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('Entrar/', LoginView.as_view(template_name='login.html'), name="login"),
    path('catalogo/', include('catalog.urls', namespace='catalog')),
    path('admin/', admin.site.urls),
]

