from django.shortcuts import render
from .models import Faq

# Create your views here.


def about(request):
    """
    This view will return the about page
    """

    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'about/about.html', context)
