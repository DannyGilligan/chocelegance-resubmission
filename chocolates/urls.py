from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chocolates, name='chocolates'),
    path('<int:chocolate_id>/', views.chocolate_detail, name='chocolate_detail'),
    path('add/', views.add_chocolate, name='add_chocolate'),
    path('edit/<int:chocolate_id>/', views.edit_chocolate, name='edit_chocolate'),
]