from django.shortcuts import render

# Create your views here.


def index(request):
    """
    This view will return the about page
    """
    return render(request, 'about/about.html')
