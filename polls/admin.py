from django.contrib import admin
from .models import Autor, Categoria, Postagem, Comentario, Video

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(Video)