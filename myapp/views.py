from django.shortcuts import render
from .models import Biblioteca, Libro
from .forms import NuevoLibroForm

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html', {
        'title': title
    })

def lista_bibliotecas(request):
    # Obtener todas las bibliotecas
    bibliotecas = Biblioteca.objects.all()

    # Renderizar el template
    return render(request, 'lista_bibliotecas.html', {'bibliotecas': bibliotecas})

def detalles_biblioteca(request, biblioteca_id):
    # Obtener la biblioteca
    biblioteca = Biblioteca.objects.get(pk=biblioteca_id)

    # Obtener todos los libros de la biblioteca
    libros = Libro.objects.filter(biblioteca=biblioteca)

    # Renderizar el template
    return render(request, 'detalles_biblioteca.html', {'biblioteca': biblioteca, 'libros': libros})

def nuevo_libro(request, biblioteca_id):


    # Obtener la biblioteca
    biblioteca = Biblioteca.objects.get(pk=biblioteca_id)

    # Crear un nuevo formulario de libro
    if request.method == 'POST':
        form = NuevoLibroForm(request.POST)
        if form.is_valid():
            # Crear un nuevo libro
            libro = Libro()
            libro.biblioteca = biblioteca
            libro.nombre = form.cleaned_data['nombre']
            libro.isbn = form.cleaned_data['isbn']
            libro.autor = form.cleaned_data['autor']
            libro.estado = form.cleaned_data['estado']
            libro.save()

            # Redirigir a la página de detalles de la biblioteca
            return HttpResponseRedirect(reverse('detalles_biblioteca', args=[biblioteca.id]))
    else:
        form = NuevoLibroForm()

    # Renderizar el template
    return render(request, 'nuevo_libro.html', {'biblioteca': biblioteca, 'form': form})