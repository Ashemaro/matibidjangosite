from django.contrib import admin
from django.urls import path
from . import views

app_name = 'friendsformatibi'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('runningprojects/', views.runningprojects, name='runningprojects'),
    path('projectstofund/', views.projectstofund, name='projectstofund'),
    path('completedprojects/', views.completedprojects, name='completedprojects'),
]