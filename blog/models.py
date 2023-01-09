from django.db import models
from django.contrib.auth.models import User as Usuario

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length= 30)
    contenido = models.TextField()
    fecha = models.DateField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


