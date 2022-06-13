from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileFrom


def profile(request):
    """
    Display user's profiles
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileFrom(request.POST, instance=profile)
        if form.is_valid():
            if form.save():
            messages.success(request, 'Profile updated successfully')

    form = UserProfileFrom(isinstance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'from': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
