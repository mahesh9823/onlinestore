from rest_framework import serializers
from .models import CartModel


class CartGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = "__all__"
        depth = 2


class CartInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ["buyerId", "productId", "quantity"]


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = ["quantity"]
