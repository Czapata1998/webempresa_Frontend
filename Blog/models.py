from django.db import models
from django.utils import timezone  #se importa para saber la hora de la publicacion del modelo posts
from django.contrib.auth.models import User #Trae el MODELO DE USUARIOS propio de django
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de actualización')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']  #Ordenar los archivos por fecha de creación - AL CREATED SE LE COLOCA UN - PARA QUE LOS NUEVOS ARTICULOS QUEDEN DE PRIMEROS
        
    def __str__(self):
         return self.name



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(max_length=500, verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=timezone.now)   #para que registre la hora a la que se realizo el post
    image =models.ImageField(upload_to='blog' , verbose_name='Imagen', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Fecha de actualización')
    
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-created']  #Ordenar los archivos por fecha de creación - AL CREATED SE LE COLOCA UN - PARA QUE LOS NUEVOS ARTICULOS QUEDEN DE PRIMEROS
        
    def __str__(self):
         return self.title


