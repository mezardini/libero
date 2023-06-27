from django.contrib import admin
from django.urls import path
from .views import GeneratePlayer
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('playergen/', GeneratePlayer.as_view(), name='playergen'),
]