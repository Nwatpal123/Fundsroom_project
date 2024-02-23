from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_restaurant, name='create_restaurant'),

]
