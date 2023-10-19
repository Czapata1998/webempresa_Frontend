from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import  ContactForm
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    # print("TIPO DE PETICION: {}".format(request.method))  PARA  COMPROBAR QUE SI VAYA POR POST
    contact = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            #ENVIAMOS EL CORREO Y REDIRECIONAMOS
            email = EmailMessage(
                "Café Xixaraca: Nuevo mensaje de contacto", 
                "De {} <{}> \n\nEcribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["cristhianjulian22@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
               # salio bien
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien, redirecionamos al FAIL
                 return redirect(reverse('contact')+"?fail")
           
    
    return render(request, "contact/contact.html", {'form': contact})