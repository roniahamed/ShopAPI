from django.urls import path
from .views import HomeAPIView, ProductListAPIView

urlpatterns = [
    path('',HomeAPIView.as_view(), name='home'),
    path('products/', ProductListAPIView.as_view(), name='products' ),
]
