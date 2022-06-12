from django.shortcuts import render, get_object_or_404 

from .models import UserProfile
from .forms import UserProfileFrom


def profile(request):
    """
    Display user's profiles
    """
    profile = get_object_or_404(UserProfile, user=request.user)


    form = UserProfileFrom(isinstance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'from': form,
        'orders': orders,
    }

    return render(request, template, context)
