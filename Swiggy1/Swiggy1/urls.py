from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('Userprofile.urls')),
    path('restaurant/', include('Restaurant.urls')),
    path('neworder/', include('Neworder.urls')),
    path('partner/', include('Deliverypartner.urls')),
    
 
    
    
 
 
]
