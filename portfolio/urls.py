from django.shortcuts import render
from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('apresentacao', views.apresntacao_page_view, name='apresentacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('formacao', views.formacao_page_view, name='formacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('noticias', views.noticias_page_view, name='noticias'),
    path('contacto', views.contacto_page_view, name='contacto'),
]