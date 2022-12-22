"""Practica URL Configuration

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
# Importar mis módulos/apps
from Practica.views import saludo, saludo_html, despedida, get_fecha, calcular_edad, curso
from gestionPedidos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",saludo),                                     # Agrego mis paths "" es el punto de entrada
    path("saludohtml/",saludo_html),
    path("despedida/",despedida),
    path("fecha/",get_fecha),
    path("edades/<int:edad>/<int:agno>",calcular_edad),   # Pasar por parámetros
    path("curso/",curso),
    path('busqueda_productos/',views.busqueda_productos),
    path('buscar/',views.buscar),   
    path('contacto/',views.contacto),
]
