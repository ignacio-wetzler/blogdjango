from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as Usuario
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length= 30)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentaristas = models.ManyToManyField(Usuario, related_name= "comentaristas", blank = True )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("post-detail", kwargs = {"pk": self.pk})

class Comentario(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-fecha"]
    
    def __str__(self):
        return self.contenido[0:50]