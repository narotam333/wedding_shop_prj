from django.db import models

# Create your models here.

class ProductList(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100, primary_key=True)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    in_stock_quantity = models.IntegerField()


class GiftList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(ProductList, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, default="XYZ")
    price = models.DecimalField(max_digits = 7, decimal_places = 2, default=999)
    available_quantity = models.IntegerField(default=0)
    purchased_quantity = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(GiftList, self).save(*args, **kwargs)
