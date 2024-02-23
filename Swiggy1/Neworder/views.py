from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Order
from Userprofile.models import User
from Restaurant.models import Restaurant
from django.db.models import Max

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        # Parse the JSON data from the request
        data = JSONParser().parse(request)
        
        # Extract userid and restaurantid from the data
        user_id = data.get('userid')
        restaurant_id = data.get('restaurantid')

        # Check if the user exists
        try:
            user = User.objects.get(userid=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)

        # Check if the restaurant exists
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            return JsonResponse({'error': 'Restaurant does not exist'}, status=404)

        # Get the maximum delivery_groupid for the restaurant
        existing_orders = Order.objects.filter(restaurantid=restaurant)
        max_groupid = existing_orders.aggregate(Max('delivery_groupid'))['delivery_groupid__max']


        # Create the order
        order = Order.objects.create(
            userid=user,
            restaurantid=restaurant,
            delivery_address=data.get('delivery_address'),
            delivery_groupid=max_groupid + 1 if max_groupid is not None else 1
        )

        return JsonResponse({'message': 'Order created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
