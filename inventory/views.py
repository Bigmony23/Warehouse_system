from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.models import Product_Material, Product, Material
from inventory.serializers import ProductSerializer, Product_MaterialSerializer


class PostProductsView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success',
                             'data':request.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Product_MaterialsView(APIView):
    def post(self, request):
        product=get_object_or_404(Product,id=request.data['product_id'])
        material=get_object_or_404(Material,id=request.data['material_id'])
        quantity=request.data['quantity']
        if quantity<=0:
            return Response({'error': 'quantity must be greater than zero',
                             },status=400)
        product_materials = Product_Material.objects.create(
            product_id=product,
            material_id=material,
            quantity=quantity,
        )
        serializer = Product_MaterialSerializer(product_materials)
        return Response({'status': 'success',
                         'data':serializer.data}, status=status.HTTP_200_OK)













# Create your views here.
