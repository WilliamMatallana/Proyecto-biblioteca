from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bibliotecas/', views.lista_bibliotecas, name='lista_bibliotecas'),
    path('bibliotecas/<int:biblioteca_id>/', views.detalles_biblioteca, name='detalle_biblioteca'),
    path('bibliotecas/<int:biblioteca_id>/agregar_libro/', views.nuevo_libro, name='agregar_libro'),
]
