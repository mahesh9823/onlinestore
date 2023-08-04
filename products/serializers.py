from rest_framework import serializers
from .models import ProductModel
# from categories.serializers import CategoryGetSerializer
# from sellers.serializers import SellerGetSerializer


class ProductGetSerializer(serializers.ModelSerializer):
    # category = CategoryGetSerializer()
    # seller = SellerGetSerializer()

    class Meta:
        model = ProductModel
        fields = "__all__"
        depth = 1


class ProductInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["categoryId", "sellerId", "productName", "productDetails", "productPrice", "productStock"]


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["categoryId", "productName", "productDetails", "productPrice", "productStock"]
