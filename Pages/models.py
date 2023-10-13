from typing import Any
from django.db import models

# Create your models here.

class Page (models.Model):
    name = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(max_length=5000, verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["order", "name"]
    
    def __str__(self):
        return self.name
