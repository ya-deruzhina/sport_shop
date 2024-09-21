from rest_framework import serializers
from apps.shop.serializers.catalog.category import SubCategorySearchSerializer,CategorySearchSerializer


class GoodsSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField (read_only = True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    amount = serializers.IntegerField()
    category = CategorySearchSerializer()
    subcategory = SubCategorySearchSerializer()

