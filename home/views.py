# Create your views here.
from multiprocessing import context
from django.shortcuts import render
import torch
import cv2,os
import numpy as np

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

from .detect import detect
from django.conf import settings
global namex
def index(request):
    contxt = {}
    return render(request, 'home/home.html',contxt)

def services(request):
    contxt = {}
    return render(request, 'home/services.html',contxt)











def image_upload(request):
    
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            imageURL = settings.MEDIA_URL + form.instance.main_Img.name
            namex = detect(settings.MEDIA_ROOT_URL + imageURL)
            images = Image.objects.latest('id')
            contxt = {'images': images,
                  'namex' : namex}
            print(contxt)
            return render(request, 'home/display_images.html',contxt)
    else:
        form = ImgForm()
    contxt = {'form': form}
    return render(request, 'home/gender.html', contxt)
 
def success(request): 
    return HttpResponse('successfully uploaded')

def display_images(request):
    if request.method == 'GET':
        # getting all the objects 
        images = Image.objects.latest('id')
        contxt = {'images': images,
                  'namex' : namex}


    return render(request, 'home/display_images.html',contxt)



