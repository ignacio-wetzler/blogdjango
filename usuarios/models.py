from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = fr"avatars\avatarpordefecto.png", upload_to = fr"avatars")

    def __str__(self):
        return f"Perfil de {self.user.username}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to = "avatars")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"Perfil de {self.user.username}"