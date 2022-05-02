from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """this will ring customers to their shopping bag, (Home) page"""
    
    return render(request, 'bag/bag.html')