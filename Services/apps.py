from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Services'
    verbose_name= 'Gestor de servicios'   #para cambiar el nombre en el admin
