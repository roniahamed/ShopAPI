from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import TagSerializer, BrandSerializer, CategorySerializer, ProductSerializer
from .models import Product, Tag, Brand, Category
from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

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

            response_data = {
            'messages':'Successfully adding your Products',
            'products':serializer.data
            } 

            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailsProductAPIView(APIView):

    def get_object(self, pk):

        try:
            return Product.objects.select_related('brand', 'category').prefetch_related('tags').get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        response_data = {
            'message':'Deleted Successfully'
        }
        return Response(response_data,status=status.HTTP_204_NO_CONTENT)
        
# Generic views 

class ProductListView(generics.ListCreateAPIView):
    queryset = queryset = Product.objects.select_related('brand', 'category').prefetch_related('tags').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = Product.objects.select_related('brand', 'category').prefetch_related('tags').all()
    serializer_class = ProductSerializer
    filterset_fields = ['category', 'brand', 'tags']
