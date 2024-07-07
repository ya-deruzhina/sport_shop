from rest_framework import serializers
from apps.shop.models import ProductInOrder
        
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrder
        fields = ['order','product','count','price_one']
        
        def create(self, validated_data):
            return ProductInOrder.objects.create(**validated_data)