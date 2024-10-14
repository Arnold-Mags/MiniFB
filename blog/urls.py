from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bl-home'),
    path('about/', views.about, name='bl-about'),
]