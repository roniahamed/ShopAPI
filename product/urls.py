from django.urls import path
from .views import HomeAPIView, ProductListAPIView, DetailsProductAPIView, ProductListView, ProductDetailview
urlpatterns = [
    path('',HomeAPIView.as_view(), name='home'),
    path('products/', ProductListAPIView.as_view(), name='products' ),
    path('products/<int:pk>/', DetailsProductAPIView.as_view(), name='product' ),

    path('products/generic/', ProductListView.as_view(), name='products-generic' ),
    path('product/<int:pk>/', ProductDetailview.as_view(), name='product-details' ),
]
