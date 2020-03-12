from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('services/', views.services),
    path('portfolio_details/', views.portfolio_details),
    path('blog/', views.blog),
    path('blog-details/', views.blog_details),
    path('contact/', views.contact),
    
   


]