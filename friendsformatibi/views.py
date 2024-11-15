from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def runningprojects(request):
    return render(request, 'runningprojects.html')


def projectstofund(request):
    return render(request, 'projectstofund.html')


def completedprojects(request):
    return render(request, 'completedprojects.html')
