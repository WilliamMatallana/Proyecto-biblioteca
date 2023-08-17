from django.db import models

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    autor = models.CharField(max_length=50)
    estado = models.CharField(max_length=8)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
