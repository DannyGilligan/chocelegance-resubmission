from django.shortcuts import render
from testimonials.models import Testimonial

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


def privacypolicy(request):
    """
    This simple view will return the privacy policy page
    """
    return render(request, 'home/privacy.html')


def terms(request):
    """
    This simple view will return the terms and conditions page
    """
    return render(request, 'home/terms.html')
