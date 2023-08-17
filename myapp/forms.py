from django import forms
from .models import Biblioteca, Libro

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['nombre', 'ubicacion']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'isbn', 'autor', 'estado']

class NuevoLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'isbn', 'autor', 'estado']
