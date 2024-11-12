from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('news/', views.news, name='news'),
    path('nookhubactivities/', views.nookhub, name='nookhubactivities'),
]