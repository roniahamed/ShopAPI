from rest_framework import serializers
from .models import Product, Category, Brand, Tag, Review   
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
