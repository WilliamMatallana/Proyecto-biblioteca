from django.shortcuts import render
from .models import Biblioteca, Libro
from .forms import NuevoLibroForm

def index( request ):
    title = "Bienvenido!!"
    return render(request, 'index.html', {
        'title': title
    })

def lista_bibliotecas( request ):
    return render(request, 'bibliotecas/biblioteca.html')

def agregar_biblioteca(request):
    # Obtener todas las bibliotecas
    bibliotecas = Biblioteca.objects.all()

    # Renderizar el template
    return render(request, 'bibliotecas/agregar_biblioteca.html', {'bibliotecas': bibliotecas})


def lista_libros (request):
    return render(request, 'libros/libro.html')

def agregar_libros(request):
    # Obtener todas los libros
    libros = Libro.objects.all()

    # Renderizar el template
    return render(request, 'libros/agregar_biblioteca.html', {'libros': libros})

