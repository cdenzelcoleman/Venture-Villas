from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Resort
from django.contrib.auth.decorators import login_required
import random

class Home(LoginView):
    template_name = 'home.html'

def home_resorts(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    if request.user.is_authenticated:
        resorts = list(Resort.objects.all())
        random_resort = random.sample(resorts, min(len(resorts), 6))
        return render(request, 'home.html', {'resorts': random_resort})
    else:
        return render(request, 'home.html', {'form': form})

def home(request):
    form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})

def resorts_page(request):
    resorts = Resort.objects.all()
    return render(request, 'resorts_page.html', {'resorts': resorts})

@login_required
def favorite_resorts(request):
    favorite_resorts = request.user.favorite_resorts.all()
    return render(request, 'favorite_resorts.html', {'resorts': favorite_resorts})

@login_required
def add_favorite(request, resort_id):
    resort = get_object_or_404(Resort, id=resort_id)
    resort.favorite_by.add(request.user)
    return redirect('resorts-page')

@login_required
def remove_favorite(request, resort_id):
    resort = get_object_or_404(Resort, id=resort_id)
    resort.favorite_by.remove(request.user)
    return redirect('favorite-resorts')

def reservations(request):
    return render(request, 'reservations.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    
def resort_detail(request, resort_id):
    resort = get_object_or_404(Resort, id=resort_id)
    return render(request, 'resort_detail.html', {'resort': resort})