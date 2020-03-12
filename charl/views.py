from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def login(request):
    return render(request, 'charl/login.html')

def home(request):
    return render(request, 'charl/home.html')

def profile(request):
    return render(request, 'charl/profile.html')

def gallery(request):
    return render(request, 'charl/gallery.html')

def contact(request):
    return render(request, 'charl/contact.html')