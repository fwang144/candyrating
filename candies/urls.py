from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('candies/', views.candies, name='candies'),
    path('candies/details/<int:id>', views.details, name='details'),
    path('candies/addcandy', views.addcandy, name='addcandy'),
    path('candies/edit/<int:id>', views.editcandy, name='editcandy'),
    path('candies/editprocess/<int:id>', views.editcandyprocess, name="editcandyprocess"),
    path('candies/details/delete/<int:id>', views.delete, name='delete'),
]