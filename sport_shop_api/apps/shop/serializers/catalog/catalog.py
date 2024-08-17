from rest_framework import serializers
from apps.shop.models import ProductsModel
from apps.shop.serializers.catalog.category import CategorySerializer, SubCategorySerializer
        
class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsModel
        category = CategorySerializer()
        subcategory = SubCategorySerializer()
        # fields = ['name','description','price','amount','category','subcategory']
        fields ='__all__'
                
        def create(self, validated_data):
            return ProductsModel.objects.get_or_create(**validated_data) 
