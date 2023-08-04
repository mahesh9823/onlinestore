from rest_framework import serializers
from .models import SellerModel


class SellerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = "__all__"


class SellerInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = ["sellerName", "sellerDetails", "sellerEmailId", "sellerPassword", "sellerContactNo"]


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = ["sellerName", "sellerDetails", "sellerPassword", "sellerContactNo"]
