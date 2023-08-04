from django.db import models


# Create your models here.

class BuyerModel(models.Model):
    buyerId = models.IntegerField(primary_key=True)
    buyerName = models.CharField(max_length=50)
    buyerDetails = models.TextField(null=True)
    buyerEmailId = models.EmailField(unique=True)
    buyerPassword = models.CharField(max_length=12)
    buyerContactNo = models.CharField(max_length=12)

    def __str__(self):
        return self.buyerName
