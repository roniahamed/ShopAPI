from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView

class HomeAPIView(APIView):

    def get(self, request, format=None):

        data = {'message': 'Welcome to ShopAPI!', 'version':'1.0'}

        return Response(data, status=status.HTTP_200_OK)
        