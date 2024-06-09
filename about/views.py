from django.shortcuts import render

# Create your views here.


def about(request):
    """
    This view will return the about page
    """

    faqs = Faq.objects.all()

    context = {
        'faqs': faqs,
    }
    
    return render(request, 'about/about.html')
