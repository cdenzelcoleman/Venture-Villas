from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Resort
import random

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def home_resorts(request):
    if request.user.is_authenticated:
        resorts = list(Resort.objects.all())
        random_resort = random.sample(resorts, min(len(resorts), 6))
        return render(request, 'home.html', {'resorts': random_resort})
    else:
        form = AuthenticationForm()
        return render(request, 'home.html', {'form': form})

def home(request):
    form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})

def resorts_page(request):
    resorts = Resort.objects.all()
    return render(request, 'resorts_page.html', {'resorts': resorts})

def favorite_resorts(request):
    return render(request, 'favorite_resorts.html')

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