from django.db import models

# Create your models here.
class PostBlog(models.Model):
    nome = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    comentario = models.CharField(max_length=450)
    data = models.DateTimeField(auto_now_add=True)

class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

