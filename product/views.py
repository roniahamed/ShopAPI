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
        products = Product.objects.select_related('brand', 'category').prefetch_related('tags').all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            validated_data = serializer.validated_data

            response_data = {
            'messages':'Successfully adding your Products',
            'products':validated_data
            } 

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
