from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    #imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentário por {self.nome} em {self.postagem}"

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    url = models.URLField()
    postagem = models.OneToOneField(Postagem, on_delete=models.CASCADE, related_name='video')

    def __str__(self):
        return self.titulo