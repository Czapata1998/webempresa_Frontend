from django.contrib import admin
from  .models import Service
# Register your models here.


class AdminService(admin.ModelAdmin):
    list_display = ('title', 'Subtitle', 'content', 'image', 'created', 'updated')
    readonly_fields = ('created', 'updated')


admin.site.register(Service, AdminService)