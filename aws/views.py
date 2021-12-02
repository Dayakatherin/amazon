from django.shortcuts import render,redirect
from .models import  Photo

def addPhoto(request):

    if request.method == 'POST':
        images = request.FILES.get('images')
        photo = Photo.objects.create(
        image=images,
            )
    return render(request, 'photos/add.html',photo)