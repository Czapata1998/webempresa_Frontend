from django.contrib import admin
from .models import  Link
# Register your models here.

class AdminLink(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    
    
    
admin.site.register(Link, AdminLink)
