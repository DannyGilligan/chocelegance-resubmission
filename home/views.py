from django.shortcuts import render
from .models import Testimonial

# Create your views here.


def index(request):
    """
    This view will return the index page
    """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)
