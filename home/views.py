from django.shortcuts import render
"""
Provides some arithmetic functions
"""

# Create your views here.

def index(request):
    """this will show the view for the index, (Home) page"""

    return render(request, 'home/index.html')
