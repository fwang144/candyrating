from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('candies/', views.candies, name='candies'),
    path('candies/details/<int:id>', views.details, name='details'),
]