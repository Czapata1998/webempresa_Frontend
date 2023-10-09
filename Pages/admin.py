from django.contrib import admin
from .models import Page
# Register your models here.


class AdminPage(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    search_fields = ( 'name', 'created', 'updated')
    
admin.site.register(Page, AdminPage)
    