from django.urls import path, include
from .views import indice, acerca, bienvenido,contacto,exito,register

urlpatterns = [
    path('', indice, name="index"),
    path('acerca/', acerca, name="about"),
    path('bienvenido/', bienvenido, name="welcome"),
    path('contacto/', contacto, name="contact"),
    path('exito/', exito, name="success" ),
    path('accounts/', include("django.contrib.auth.urls")),
    path('registro/', register, name='register'),
]