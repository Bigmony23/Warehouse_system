from collections import defaultdict

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.models import Product_Material, Product, Material, Warehouse
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

class WarehouseView(APIView):
    def post(self, request):
        result=[]
        used_from_warehouse = defaultdict(int)
        for req in request.data:
            product=get_object_or_404(Product,
                                      product_code=req['product_code'])
            quantity=req['quantity']
            product_materials=Product_Material.objects.filter(product_id=product)
            materials_result=[]
            for pm in product_materials:
                total_qty=pm.quantity*quantity
                material=pm.material_id


                warehouses=Warehouse.objects.filter(
                    material_id=material,
                    remainder__gt=0
                ).order_by('id')

                remaining_needed=total_qty
                for w in warehouses:
                    if remaining_needed<=0:
                        break
                    available=w.remainder-used_from_warehouse[w.id]
                    if available<=0:
                        continue

                    take=min(remaining_needed,w.remainder)
                    used_from_warehouse[w.id]+=take
                    remaining_needed-=take
                    materials_result.append({
                        "warehouse_id": w.id,
                        "material_id": material.material_name,
                        "qty": take,
                        "price": w.price,
                    })



                if remaining_needed>0:
                    materials_result.append({
                            "warehouse_id":None,
                            "material_id":material.material_name,
                            "qty":remaining_needed,
                            "price":None,
                        }
                    )





            result.append({
                "product_name":product.product_name,
                "product_qty":quantity,
                "product_materials":materials_result,

            })
        return Response({"result":result},status=status.HTTP_200_OK)

















# Create your views here.
