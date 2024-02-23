from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from rest_framework import generics
from .serializers import UserSerializer
import json

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        address = data.get('address')
        userid = data.get('userid')

        if name and email and password and address and userid:
            # Create user
            user = User.objects.create(name=name, email=email, password=password, address=address, userid=userid)
            response_data = {'message': 'User created successfully'}
            return JsonResponse(response_data, status=201)
        else:
            response_data = {'error': 'All fields are required'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=405)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
