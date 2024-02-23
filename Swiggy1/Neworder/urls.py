from django.urls import path
from . import views

urlpatterns = [
    path('create2/', views.create_order, name='create_order'),
    # Add more paths as needed
]