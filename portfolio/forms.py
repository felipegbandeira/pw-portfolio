from django.forms import ModelForm
from .models import PostBlog
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = PostBlog
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome',
            'titulo': 'Titulo',
            'comentario': 'Comentário',
        }