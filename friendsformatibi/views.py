from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def nookhub(request):
    return render(request, 'nookhub.html')


def news(request):
    return render(request, 'news.html')
