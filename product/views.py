from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import TagSerializer, BrandSerializer, CategorySerializer, ProductSerializer

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