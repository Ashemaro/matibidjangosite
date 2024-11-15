from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view, create_post


app_name = 'matibisiteblog'

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('news/', views.news, name='news'),
    path('news_details', views.news_details, name='news_details'),
    path('nookhubactivities/', views.nookhub, name='nookhubactivities'),
    path('login/', login_view, name='login'),
]