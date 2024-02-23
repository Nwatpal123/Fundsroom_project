from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('users/', views.UserList.as_view(), name='user-list'),
]
