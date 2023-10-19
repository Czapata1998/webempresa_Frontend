from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import  Link
# Register your models here.

class AdminLink(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="PERSONAL").exists():
            return  ('created', 'updated', 'key', 'name')
        else:
            return  ('created', 'updated')
        
admin.site.register(Link, AdminLink)
