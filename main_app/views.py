from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def resorts_page(request):
    return render(request, 'resorts_page.html')

def favorite_resorts(request):
    return render(request, 'favorite_resorts.html')

def reservations(request):
    return render(request, 'reservations.html')
