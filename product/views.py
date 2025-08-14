from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import TagSerializer, BrandSerializer, CategorySerializer, ProductSerializer
from .models import Product, Tag, Brand, Category

class HomeAPIView(APIView):

    def get(self, request, format=None):

        data = {'message': 'Welcome to ShopAPI!', 'version':'1.0'}

        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        received_data = request.data 
        print(received_data)
        
        response_data = {
            'message':'Data received successfully!',
            'my_data': received_data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
# list apiview

class ProductListAPIView(APIView):

    def get(self, request, format = None):
        # products = Product.objects.all()

        response_data = {
            'messages':'This is our products list',
            'products':[{'id': 1, 'name': 'Laptop'}, {'id': 2, 'name': 'Mouse'}]
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        receive_data = request.data 

        response_data = {
            'messages':'Successfully adding your Products',
            'products':receive_data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
