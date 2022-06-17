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


class Linguagem(models.Model):
    nome = models.CharField(max_length=50)
    proficiencia = models.CharField(max_length=50)
    referencias = models.CharField(max_length=300)


class Professor(models.Model):
    nome = models.CharField(max_length=20)
    link = models.CharField(max_length=500)


class Interesse(models.Model):
    titulo = models.CharField(max_length=50)
    descicao = models.CharField(max_length=500)


class Projeto(models.Model):
    titulo = models.CharField(max_length=50)
    descicao = models.CharField(max_length=500)
    ano = models.IntegerField()


class Cadeira(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField()
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
    projetos = models.ManyToManyField(Projeto)


class Tfc(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.CharField(max_length=50)
    orientadores = models.CharField(max_length=50)
    ano = models.IntegerField()
    resumo = models.CharField(max_length=500)
    relatorio = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    imagem = models.CharField(max_length=500)
    video = models.CharField(max_length=500)

class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    acronimo = models.CharField(max_length=6)
    ano = models.IntegerField()
    criador = models.CharField(max_length=50)

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    imagem = models.CharField(max_length=500)

