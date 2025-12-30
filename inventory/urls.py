from django.urls import path

from inventory.views import PostProductsView, Product_MaterialsView, WarehouseView

urlpatterns=[
    path('product/',PostProductsView.as_view(),name='inventory'),
    path('product/materials/',Product_MaterialsView.as_view(),name='product-materials'),
    path('product/warehouse/',WarehouseView.as_view(),name='warehouse'),
]