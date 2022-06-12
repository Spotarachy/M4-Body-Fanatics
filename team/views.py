from django.shortcuts import render


def team(request):
    """
    Display user's profiles
    """

    return render(request, 'team/team.html')
    # template = 'profiles/profile.html'
    context = {}

    return render(request, )