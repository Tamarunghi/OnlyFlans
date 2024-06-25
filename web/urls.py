from django.urls import path
from .views import indice, acerca, bienvenido

urlpatterns = [
    path('', indice, name="index"),
    path('acerca/', acerca, name="about"),
    path('bienvenido/', bienvenido, name="welcome"),
]