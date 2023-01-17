from django import forms
from .models import Comentario


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["contenido"]