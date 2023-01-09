from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Profile

class FormularioAlta(UserCreationForm):
    username = UsernameField(label='Usuario')
    #password1 = forms.CharField(label="Costraseña")
    #email = forms.EmailField(label='e-mail')

    class Meta:
        model = User 
        fields = ["username","email","password1","password2"]

class FormModificacionUsuario(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","email"]

class FormModificacionPerfil(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]