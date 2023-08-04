from django.db import models
from buyers.models import BuyerModel
from products.models import ProductModel


# Create your models here.

class CartModel(models.Model):
    cartId = models.IntegerField(primary_key=True)
    buyerId = models.ForeignKey(BuyerModel, on_delete=models.CASCADE, related_name="buyers")
    productId = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="products", unique=True)
    quantity = models.IntegerField()
