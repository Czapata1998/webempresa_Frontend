from django.urls import path
from .   import views

urlpatterns = [
    path('', views.servicies, name="services"),
  
]