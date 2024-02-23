from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_restaurant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        restaurant_id = data.get('restaurant_id')
        restaurant_name = data.get('restaurant_name')
        address = data.get('address')

        if restaurant_id and restaurant_name and address:
            # Create restaurant
            new_restaurant = Restaurant(restaurantid=restaurant_id, restaurantname=restaurant_name, address=address)
            new_restaurant.save()  # Save the new restaurant instance to the database
            
            response_data = {'message': 'Restaurant created successfully'}
            return JsonResponse(response_data, status=201)
        else:
            response_data = {'error': 'Restaurant id, name, and address are required'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=405)
