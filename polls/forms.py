from django import forms
from .models import Comentario, Categoria

class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = ['nome', 'email', 'conteudo']

class CategoriaForm(forms.ModelForm):
  class Meta:
    model = Categoria
    fields = ['nome']