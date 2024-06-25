from django.urls import path
from .views import indice, acerca, bienvenido,contacto,exito

urlpatterns = [
    path('', indice, name="index"),
    path('acerca/', acerca, name="about"),
    path('bienvenido/', bienvenido, name="welcome"),
    path('contacto/', contacto, name="contact"),
    path('exito/', exito, name="success" )
]