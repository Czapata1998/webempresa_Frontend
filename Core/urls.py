from django.urls import path
from .   import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('services/', views.servicies, name="services"),
    path('sample/', views.sample, name="sample"),
]
