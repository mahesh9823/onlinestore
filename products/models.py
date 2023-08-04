from django.db import models
from categories.models import CategoryModel
from sellers.models import SellerModel


# Create your models here.
class ProductModel(models.Model):
    productId = models.IntegerField(primary_key=True)
    categoryId = models.ForeignKey(CategoryModel, related_name="categories", on_delete=models.CASCADE)
    sellerId = models.ForeignKey(SellerModel, related_name="sellers", on_delete=models.CASCADE)
    productName = models.CharField(max_length=50, unique=True)
    productDetails = models.TextField()
    productPrice = models.IntegerField(default=0)
    productStock = models.IntegerField(default=0)

    def __str__(self):
        return self.productName
