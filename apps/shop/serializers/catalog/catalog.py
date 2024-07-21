from rest_framework import serializers
from apps.shop.models import GoodsModel
from apps.shop.serializers.catalog.category import CategorySerializer, SubCategorySerializer

class CatalogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()
    class Meta:
        model = GoodsModel
        fields = ["id","name","description","price","amount","category","subcategory"]
                
        def create(self, validated_data):
            return GoodsModel.objects.create(**validated_data)