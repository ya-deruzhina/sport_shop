from rest_framework import serializers
from apps.users.models import ProductInOrder
        
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrder
        fields = ['order','pizza','count','price_one']
        
        def create(self, validated_data):
            return ProductInOrder.objects.create(**validated_data)