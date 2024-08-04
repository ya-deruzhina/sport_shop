from rest_framework import serializers
from apps.shop.models import GoodsModel
from apps.shop.serializers.catalog.category import CategorySerializer, SubCategorySerializer
        
class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsModel
        category = CategorySerializer()
        subcategory = SubCategorySerializer()
        fields = ["id","name","description","price","amount","category","subcategory"]
                
        def create(self, validated_data):
            return GoodsModel.objects.get_or_create(**validated_data)