from django.urls import path, include
from .views import HomeAPIView, ProductListAPIView, DetailsProductAPIView, ProductListView, ProductDetailview, ProductListViewSets, TagListView, BrandListView, CategoryListView, ReviewListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'products', ProductListViewSets, basename='product')
router.register(r'tags', TagListView, basename='tag')
router.register(r'brands', BrandListView, basename='brand')
router.register(r'categories', CategoryListView, basename='category')  
router.register(r'reviews', ReviewListView, basename='review')

urlpatterns = [
    path('',HomeAPIView.as_view(), name='home'),
    # path('products/', ProductListAPIView.as_view(), name='products' ),
    # path('products/<int:pk>/', DetailsProductAPIView.as_view(), name='product' ),

    # path('products/generic/', ProductListView.as_view(), name='products-generic' ),
    # path('product/<int:pk>/', ProductDetailview.as_view(), name='product-details' ),
    path('', include(router.urls)),
]
