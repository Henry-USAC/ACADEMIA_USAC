from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Ejemplo de una ruta para la vista 'home'
    # Agrega más rutas según sea necesario
]
