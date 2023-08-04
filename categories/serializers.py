from rest_framework import serializers
from .models import CategoryModel


class CategoryGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class CategoryInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["categoryName"]

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["categoryName"]
