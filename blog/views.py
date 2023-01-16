from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post
from usuarios.views import ObtenerAvatar
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from usuarios.models import Avatar


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


