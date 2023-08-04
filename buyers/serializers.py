from rest_framework import serializers
from .models import BuyerModel


class BuyerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = "__all__"


class BuyerInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = ["buyerName", "buyerDetails", "buyerEmailId", "buyerPassword", "buyerContactNo"]


class BuyerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = ["buyerName", "buyerDetails", "buyerPassword", "buyerContactNo"]
