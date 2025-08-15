from django.urls import path
from .views import HomeAPIView, ProductListAPIView, DetailsProductAPIView

urlpatterns = [
    path('',HomeAPIView.as_view(), name='home'),
    path('products/', ProductListAPIView.as_view(), name='products' ),
    path('products/<int:pk>/', DetailsProductAPIView.as_view(), name='product' ),
]
