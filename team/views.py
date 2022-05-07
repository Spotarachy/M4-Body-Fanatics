from django.shortcuts import render

# Create your views here.


def team(request):
    """thiswill show the view for the index, (Home) page"""
    
    return render(request, 'team/team.html')