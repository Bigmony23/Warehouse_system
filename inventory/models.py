from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code=models.IntegerField(unique=True)

    def __str__(self):
        return self.product_name



class Material(models.Model):
    material_name = models.CharField(max_length=100)

    def __str__(self):
        return self.material_name

class Product_Material(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='materials')
    material_id=models.ForeignKey(Material,on_delete=models.CASCADE)
    quantity=models.FloatField()


class Warehouse(models.Model):
    material_id=models.ForeignKey(Material,on_delete=models.CASCADE,related_name='warehouses')
    remainder=models.FloatField()
    price=models.FloatField()



# Create your models here.
