from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('biblioteca/', views.lista_bibliotecas, name='bibliotecas'),
    path('agregar_biblioteca/', views.agregar_biblioteca, name='agregar_biblioteca'),
    path('libro/', views.lista_libros, name='libros'),
    path('agregar_libro', views.agregar_libros, name='agregar_libros'),

]
