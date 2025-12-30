from rest_framework import serializers
from .models import Product, Product_Material, Warehouse


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Material
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'




