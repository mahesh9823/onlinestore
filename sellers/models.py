from django.db import models


# Create your models here.

class SellerModel(models.Model):
    sellerId = models.IntegerField(primary_key=True)
    sellerName = models.CharField(max_length=50)
    sellerDetails = models.TextField(null=True)
    sellerEmailId = models.EmailField(max_length=100, unique=True)
    sellerPassword = models.CharField(max_length=12)
    sellerContactNo = models.CharField(max_length=12)

    def __str__(self):
        return self.sellerName

