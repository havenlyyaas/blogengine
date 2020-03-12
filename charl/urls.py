from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('profile/', views.profile),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
   


]