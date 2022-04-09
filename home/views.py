from django.shortcuts import render
from django.db import models

# Create your views here.

def index(request):
    """The view for the index page"""
    
    return render(request, 'home/index.html')
