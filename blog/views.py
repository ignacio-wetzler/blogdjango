from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post, Comentario
from .forms import FormularioComentario
from usuarios.views import ObtenerAvatar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from usuarios.models import Avatar
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)

def about(request):
    with open(fr"media\static\about.txt") as f:
        lines = f.readlines()
    cita = "Liber - ICAPUT 1"
    imagen = fr"media\static\17_saint_augustin.jpg"
    return render(request, "blog/about.html", {"titulo": "Sobre Mi!!", "url": lines, "cita": cita, "avatar": imagen })

class VistaDeLista(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-fecha"]

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False
        


class CrearPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["titulo","contenido"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ModificarPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["titulo","contenido"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

class CrearComentario(LoginRequiredMixin, CreateView):
    model =  Comentario
    fields = ["contenido"]
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


def comentario(request, pk):
    post = Post.objects.get(id=pk)
    titulo = post.titulo
    contenido = post.contenido
    fecha = post.fecha
    autor = post.autor
    post_coments = post.comentario_set.all()
    comentaristas = post.comentaristas.all()

    if request.method == "POST":
        form_comentario = FormularioComentario(request.POST, instance = post)
        if form_comentario.is_valid():
             form_comentario.save()
             messages.success(request, f"Tu comentario ha sido gruardado exitosamente!")
        else:
            messages.success(request, f"Error en formulario!")
    else:
        form_comentario = FormularioComentario()
        
    context = {'post': post, 'titulo': titulo, 'contenido' : contenido, 'fecha' : fecha, 'autor' : autor,  'post_coments': post_coments,'comentaristas': comentaristas, "form" : form_comentario  }
    return render(request, fr'blog/comentario_form.html', context)

