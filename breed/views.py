from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'breed/index.html')

def about(request):
    return render(request, 'breed/about.html')

def portfolio(request):
    return render(request, 'breed/portfolio.html')

# Pages Menu
def services(request):
    return render(request, 'breed/services.html')

def portfolio_details(request):
    return render(request, 'breed/portfolio_details.html')


# Blog Menu
def blog(request):
    return render(request, 'breed/blog.html')

def blog_details(request):
    return render(request, 'breed/single-blog.html')


def contact(request):
    return render(request, 'breed/contact.html')

