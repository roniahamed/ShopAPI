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
        products = Product.objects.select_related('brand', 'category').prefetch_related('tags')

        product_list = []

        for product in products:
            product_list.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'category': product.category.name,
                'brand': product.brand.name if product.brand else None,
                'price': str(product.price),
                'sale_price': str(product.sale_price) if product.sale_price else None,
                'sku': product.sku,
                'stock': product.stock,
                'is_active': product.is_active,
                'image': product.get_image_url(),
                'weight': str(product.weight) if product.weight else None,
                'dimensions': product.dimensions,
                'tags': [tag.name for tag in product.tags.all()],
                'created_at': product.created_at.isoformat(),
                'updated_at': product.updated_at.isoformat()    
            })

        response_data = {
            'messages':'This is our products list',
            'products': product_list
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        receive_data = request.data 

        response_data = {
            'messages':'Successfully adding your Products',
            'products':receive_data
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
