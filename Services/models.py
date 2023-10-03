from django.db import models

# Create your models here.

class Service (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    Subtitle = models.TextField(max_length=200, verbose_name="Subtitulos")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='services/', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,)
    updated = models.DateTimeField(auto_now=True,  )
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
    
def __str__(self):
    return self.title