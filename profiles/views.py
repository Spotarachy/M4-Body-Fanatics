from django.shortcuts import render


def profile(request):
    """
    Display user's profiles
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
