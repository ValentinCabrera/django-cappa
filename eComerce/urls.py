"""eComerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

from productos.views import ProductosListView, CategoriasListView, ProductoListView, ProductosPedidosListView
from pedidos.views import PedidoAPIView, ItemPedidoAPIView, PedidosEstadosAPIView, SalonPedidosAPIView
from cocina.views import CocinaAPIView
from settings.views import SettingsAPIView

urlpatterns += [
    path('productos/', ProductosListView.as_view(), name='productos-list'),
    path('productos/<int:categoria_id>/', ProductosListView.as_view(), name='productos-list-by-categoria'),
    
    path('producto/<int:pk>/', ProductoListView.as_view()),
    path('productos/pedidos/', ProductosPedidosListView.as_view()),

    path('categorias/', CategoriasListView.as_view(), name='categorias-list'),
    path('categorias/<int:pk>/', CategoriasListView.as_view()),
   
    path('pedidos/', PedidoAPIView.as_view(), name='pedidos'),
    path('pedidos/<int:pk>/', PedidoAPIView.as_view(), name='pedido_detalle'),
    path('pedidos/<int:pk>/<int:productoId>/', PedidoAPIView.as_view()),
    path('pedidos/estados/<int:pk>/', PedidosEstadosAPIView.as_view()),

    path('salon/', SalonPedidosAPIView.as_view()),

    path('items/', ItemPedidoAPIView.as_view()),
    path('items/<int:pk>/', ItemPedidoAPIView.as_view()),

    path('cocina/', CocinaAPIView.as_view()),

    path('settings/', SettingsAPIView.as_view()),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)