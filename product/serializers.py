from rest_framework import serializers
from .models import Product, Category, Brand, Tag, Review, ProductImg
from django.contrib.auth.models import User

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'description', 'is_active', 'created_at', 'updated_at']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'is_active', 'created_at', 'updated_at']    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_active', 'created_at', 'updated_at']    

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field = 'name')
    brand = serializers.SlugRelatedField( allow_null=True, queryset = Brand.objects.all(), slug_field = 'name')
    tags = serializers.SlugRelatedField(many=True, queryset = Tag.objects.all(), slug_field='name')
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'category', 'brand', 'price','sale_price', 'discounted_price', 
            'sku', 'stock', 'is_active', 'image', 'weight', 
            'dimensions', 'tags', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'price': {'min_value': 0},
            'stock': {'min_value': 0},
        }
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Product.objects.all(),
                fields=['sku'],
                message="SKU must be unique."
            )
        ]
    def get_discounted_price(self, obj):

        if obj.sale_price is not None and obj.price > obj.sale_price:
            discount_amount = obj.price - obj.sale_price
            percentage = (discount_amount / obj.price) * 100
            return {
                'amount_saved': f"{discount_amount:.2f}",
                'percentage': f"{percentage:.2f}%",
            }
        return None

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='name')

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'rating', 'title', 'body', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'rating': {'min_value': 1, 'max_value': 5},
            'title': {'required': False},
            'body': {'required': False},
        }
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['product', 'user'],
                message="You have already reviewed this product."
            )
        ]
        
    
    def validate(self, data):
        if data.get('rating') is None:
            raise serializers.ValidationError("Rating is required.")
        if data.get('title') is None and data.get('body') is None:
            raise serializers.ValidationError("Either title or body must be provided.")
        return data

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ('id', 'title', 'created_at', 'image')
        read_only_fields = ('id', 'created_at')