from django.contrib import admin
from .models import  Category, Post

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display=('name', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    
    
class AdminPost(admin.ModelAdmin):
    list_display = ('title',  'created', 'updated', 'author', 'Post_categories') #para visusalizar una relacion manytomany es necesario poner el nombre del modelo + nombre del campo del modelo: jemplo "'Post_categories'"
    readonly_fields = ('created', 'updated',)
    search_fields = ('title', 'author__username', 'categories__name')  # Busqueda por título y nombre de usuario del autor y categoria
    ordering = ('author', 'published')
    
    def Post_categories(self, obj):  #para poder visualizar las categorias en el display
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])  #para poder visualizar las categorias en el display
    Post_categories.short_description = "Categorias"  #Para asignar un nombre personalizado en el display
    

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
