from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
        )) #Acà no se usa verboseName, se usa el label 
    email = forms.EmailField(label="Correo", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    content = forms.CharField(label="Contenido", required=True,  widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Escribe tu comentario'}))