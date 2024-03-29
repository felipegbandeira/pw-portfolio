"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('', admin.site.urls, name='home'),
    path('home', admin.site.urls, name='home'),
    path('apresentacao', admin.site.urls, name='apresentacao'),
    path('projetos', admin.site.urls, name='projetos'),
    path('formacao', admin.site.urls, name='formacao'),
    path('competencias', admin.site.urls, name='competencias'),
    path('licenciatura', admin.site.urls, name='licenciatura'),
    path('blog', admin.site.urls, name='blog'),
    path('quiz', admin.site.urls, name='quiz'),
    path('sobre', admin.site.urls, name='sobre'),
    path('noticias', admin.site.urls, name='noticias'),
    path('contacto', admin.site.urls, name='contacto'),
]