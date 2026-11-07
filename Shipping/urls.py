from django.urls import path
from Shipping import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('servicedetails/', views.servicedetails, name='servicedetails'),
    path('pricing/', views.pricing, name='pricing'),
    path('quote/', views.quote, name='quote'),
    path('contact/', views.contact, name='contact'),
    path('starterpage/', views.starterpage, name='starterpage'),
]
