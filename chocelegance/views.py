from django.shortcuts import render


def handler404(request, exception):
    """
    This view will render the 404 error
    page (Page Not Found)
    """
    return render(request, "errors/404.html", status=404)
