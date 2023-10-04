from django.db import models

# Create your models here.

class Service (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    Subtitle = models.TextField(max_length=200, verbose_name="Subtitulos")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='services', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación" )
    updated = models.DateTimeField(auto_now=True,  verbose_name="Fecha de actualización")
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created']  #Ordenar los archivos por fecha de creación - AL CREATED SE LE COLOCA UN - PARA QUE LOS NUEVOS ARTICULOS QUEDEN DE PRIMEROS
    
def __str__(self):
    return self.title