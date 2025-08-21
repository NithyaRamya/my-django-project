# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home_html'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('services.html', views.services, name='services'),
    path('projects.html', views.projects, name='projects'),
    path('contactus/', views.contactus, name='contactus'),
    path("enquiry/", views.enquiry_view, name="enquiry"),
    path('faq/', views.faq_view, name='faq'),
]
