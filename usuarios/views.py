from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FormularioAlta, FormModificacionUsuario, FormModificacionPerfil


# Create your views here.

def alta_usuario(request):
    if request.method == "POST":
        formulario_alta = FormularioAlta(request.POST)
        if formulario_alta.is_valid():
            formulario_alta.save()
            nombre = formulario_alta.cleaned_data.get("username")
            messages.success(request, f"Cuenta creada para {nombre}")
            return redirect("login")
        else:

            pass


    else:
        formulario_alta = FormularioAlta()
    return render(request, fr"blog/alta.html", {"form" : formulario_alta})

@login_required
def perfil(request):
    if request.method == "POST":
        form_usuario = FormModificacionUsuario(request.POST, instance = request.user)
        form_perfil = FormModificacionPerfil(request.POST, request.FILES, instance = request.user.profile)
        
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save ()
            messages.success(request, f"Tu cuenta ha sido modficada exitosamente!")
            return redirect("perfil")
        else:
            pass


    else:
        form_usuario = FormModificacionUsuario(instance = request.user)
        form_perfil = FormModificacionPerfil(instance = request.user.profile) 
    
    context = { "form_usuario": form_usuario, "form_perfil": form_perfil}


    return render(request, fr"blog/perfil.html", context)

