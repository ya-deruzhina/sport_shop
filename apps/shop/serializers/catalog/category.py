from rest_framework import serializers
from apps.shop.models import CategoryModel, SubCategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['category']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        fields = ['subcategory']