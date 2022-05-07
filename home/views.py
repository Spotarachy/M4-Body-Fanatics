from django.shortcuts import render


# Create your views here.

def index(request):
    """thiswill show the view for the index, (Home) page"""
    
    return render(request, 'home/index.html')