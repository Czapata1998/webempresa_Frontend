"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  #se traen estas conf por el tema de configuraciones de la media


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #PATH DE LA APP CORE 
     path('', include('Core.urls')),
     #PATH DE LA APP SERVICES
     path('services/', include('Services.urls')),
    #PATH DE LA APP BLOG 
    path('blog/', include('Blog.urls')),
    
     #PATH DE LA APP PAGES
    path('page/', include('Pages.urls')),
    
      #PATH DE LA APP CONTACT
    path('contact/', include('Contact.urls')),
  
]


if settings.DEBUG:
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT )  #toda esta configuracion es para la correcta visualizacion de las imagenes
    
    
  
    
    


    

