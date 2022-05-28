from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PictureForm
from .models import Picture
# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures}
    return render(request, '../../project_pictures/templates/media/index.html', ctx)

def upload(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

    form = PictureForm()
    ctx = {'form': form}
    return render(request, '../../project_pictures/templates/media/upload.html', ctx)

def delete(request, picture_pk):
    picture = Picture.objects.get(pk=picture_pk)
    picture.delete()
    return redirect(reverse('media:index'))