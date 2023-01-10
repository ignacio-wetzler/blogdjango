from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import Post



# Create your views here.

def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"titulo": "Sobre Mi!!"})

class VistaDeLista(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-fecha"]

class VistaDelPost(DetailView):
    model = Post

class CrearPost(CreateView):
    model = Post
    fields = ["titulo","contenido","fecha"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)