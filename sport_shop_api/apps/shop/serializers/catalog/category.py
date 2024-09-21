from rest_framework import serializers
from apps.shop.models import CategoryModel, SubCategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['category']
                        
        def create(self, validated_data):
            return CategoryModel.objects.get_or_create(**validated_data)

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryModel
        id_parent = CategorySerializer()
        fields = ['subcategory','id_parent']
                
        def create(self, validated_data):
            return SubCategoryModel.objects.get_or_create(**validated_data)

class CategorySearchSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=20)
    
class SubCategorySearchSerializer(serializers.Serializer):
    subcategory = serializers.CharField(max_length=20)
    