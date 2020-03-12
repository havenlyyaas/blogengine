from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('profile/', views.profile),
    path('blog/', views.blog),
    path('team/', views.team),
    path('contact/', views.contact),
]
 
