from django.contrib import admin

from inventory.models import Product, Material, Warehouse, Product_Material


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'id')
    search_fields = ('product_name', 'product_code')

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name','id')


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material_id','remainder','price')

class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product_id','material_id','quantity')

admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Product_Material, ProductMaterialAdmin)



# Register your models here.
