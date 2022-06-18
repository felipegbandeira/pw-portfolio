from django.shortcuts import render
from .forms import PostForm
from .models import *
from matplotlib import pyplot as plt


# Create your views here.

def home_page_view(request):
    return render(request, 'portfolio/home.html')


def apresntacao_page_view(request):
    return render(request, 'portfolio/apresentacao.html')

def noticias_page_view(request):
    ctx = {"noticias": Noticia.objects.all()}
    return render(request, 'portfolio/noticias.html',ctx)

def contacto_page_view(request):
    return render(request, 'portfolio/contacto.html')

def projetos_page_view(request):
    ctx = {"Tfcs": Tfc.objects.all()}
    return render(request, 'portfolio/projetos.html',ctx)


def formacao_page_view(request):
    return render(request, 'portfolio/formacao.html')


def competencias_page_view(request):
    return render(request, 'portfolio/competencias.html')


def licenciatura_page_view(request):
    ano1sem1 = Cadeira.objects.filter(ano=1).filter(semestre=1).values()
    ano1sem2 = Cadeira.objects.filter(ano=1).filter(semestre=2).values()
    ano2sem1 = Cadeira.objects.filter(ano=2).filter(semestre=1).values()
    ano2sem2 = Cadeira.objects.filter(ano=2).filter(semestre=2).values()

    ctx = {'a1s1': ano1sem1, 'a1s2': ano1sem2, 'a2s1': ano2sem1, 'a2s2': ano2sem2}

    return render(request, 'portfolio/licenciatura.html',ctx)

def sobre_page_view(request):
    ctx = {'Tecs': Tecnologia.objects.all()}
    return render(request, 'portfolio/sobre.html', ctx)


def blog_page_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form, 'Posts': PostBlog.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def quiz_page_view(request):

    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
    desenha_grafico_resultados()
    return render(request, 'portfolio/quiz.html')


def desenha_grafico_resultados():
    participantes = PontuacaoQuizz.objects.all()
    lista = sorted(participantes, key=lambda x: x.pontuacao)
    nomes = []
    pontuacoes = []

    for i in lista:
        nomes.append(i.nome)
        pontuacoes.append(i.pontuacao)
    plt.barh(nomes, pontuacoes)
    plt.savefig('portfolio/static/portfolio/images/grafico.png', bbox_inches='tight')

def pontuacao_quizz(request):
    q1 = request.POST.get('Q1', False)
    q2 = request.POST.get('Q2', False)
    q3 = request.POST.get('Q3', False)
    q4_1 = request.POST.get('Q4.1', False)
    q4_2 = request.POST.get('Q4.2', False)
    q4_3 = request.POST.get('Q4.3', False)
    q4_4 = request.POST.get('Q4.4', False)
    q5 = request.POST.get('Q5', False)
    r = 0

    if q1 and q1 == 'blank':
        r += 1
    if q2 and q2 == '1':
        r += 1
    if q3 and q3 == '@media(max-width: 600px)':
        r += 1
    if q4_1 and q4_1 == 'urls':
        r += 1
    if q4_2 and q4_2 == 'views':
        r += 1
    if q4_3 and q4_3 == 'forms':
        r -= 1
    if q4_4 and q4_4 == 'models':
        r += 1
    if q5 and q5 == '<title>':
        r += 1

    return r
