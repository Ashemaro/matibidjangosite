from django.views import generic
from django.shortcuts import render, redirect, reverse
from .forms import ContactForm, NewsForm, RegistrationForm
from .models import News, VisitCounter, NookHubActivities
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixincd


class NewsList(generic.ListView):
    queryset = News.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visit_counter, created = VisitCounter.objects.get_or_create()
        if created:
            visit_counter.save()
        visit_counter.count += 1
        visit_counter.save()
        context['visit_counter'] = visit_counter
        return context


class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news_detail.html'


class NookHubActivityList(generic.ListView):
    queryset = NookHubActivities.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visit_counter, created = VisitCounter.objects.get_or_create()
        if created:
            visit_counter.save()
        visit_counter.count += 1
        visit_counter.save()
        context['visit_counter'] = visit_counter
        return context


class NookHubActivityDetail(generic.DetailView):
    model = News
    template_name = 'nookhub_detail.html'


def create_post(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            # Depending on the category selected, create the post for the corresponding model
            if category == 'News':
                News.objects.create(
                    title=form.cleaned_data['title'],
                    slug=form.cleaned_data['slug'],
                    author=form.cleaned_data['author'],
                    content=form.cleaned_data['content'],
                    status=form.cleaned_data['status'],
                    image=form.cleaned_data['image']
                )
            return redirect('matibisiteblog:create_post')
    else:
        form = NewsForm()
    return render(request, 'create_post.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('matibisiteblog:create_post')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def nookhub(request):
    return render(request, 'nookhub.html')


def news(request):
    return render(request, 'news.html')


def news_details(request):
    return render(request, 'news_details.html')
