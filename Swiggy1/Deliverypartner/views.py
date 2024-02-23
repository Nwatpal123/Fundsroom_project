from django.http import JsonResponse
from Neworder.models import Order

def get_orders_by_restaurant(request, restaurant_id):
    if request.method == 'GET':
        # Fetch orders for the specific restaurant ID
        orders = Order.objects.filter(restaurantid_id=restaurant_id)

        if orders.exists():
            orders_info = []
            for order in orders:
                # Extract order information
                
                order_info = {
                    'orderid': order.orderid,
                    'userid': order.userid_id,  # Assuming userid is the user's ID
                    'restaurantid': order.restaurantid_id,  # Assuming restaurantid is the restaurant's ID
                    'delivery_address': order.delivery_address,
                    # Add other fields as needed
                }
                orders_info.append(order_info)

            return JsonResponse({'orders': orders_info}, status=200)
        else:
            return JsonResponse({'message': 'No orders found for the specified restaurant ID'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
