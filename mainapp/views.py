from django.shortcuts import render

# Create your views here.
from .models import HomeBanner

def home(request):
    banner = HomeBanner.objects.first()
    return render(request, 'home.html', {'banner': banner})