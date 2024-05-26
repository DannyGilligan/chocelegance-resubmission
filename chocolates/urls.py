from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chocolates, name='chocolates'),
    path('<chocolate_id>', views.chocolate_detail, name='chocolate_detail'),
]