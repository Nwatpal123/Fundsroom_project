from django.urls import path
from .views import get_orders_by_restaurant
from . import views

urlpatterns = [
    path('orders/<int:restaurant_id>/', views.get_orders_by_restaurant, name='get_orders_by_restaurant'),
]
