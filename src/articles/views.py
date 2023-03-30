from django.shortcuts import render,redirect
from articles.models import Article
from menu.models import LeftSideMenu
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, TemplateView
from articles.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    articles = Article.objects.all().order_by("-created_date")
    left_side_item = LeftSideMenu.objects.all().order_by("priority")

    return render(request, 'index.html', {'left_side_item': left_side_item, 'articles': articles, })


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login', {'form' : form})

def LoginPage(request):
    return render(request, 'login.html')