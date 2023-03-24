from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('gender/', views.image_upload, name='gender'),
    path('success', success, name='success'),
    path('display_images/', views.display_images, name = 'display_images'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)