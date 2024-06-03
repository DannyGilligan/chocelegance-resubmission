from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def profile(request):
    """ Displays a template rendering the user's profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)