from rest_framework import serializers
from .models import Product, Product_Material


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Material
        fields = '__all__'



