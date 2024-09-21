from rest_framework import serializers
from apps.shop.models import ProductInOrder
        
class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrder
        # import pdb; pdb.set_trace()
        fields = ['id','order','product','count','price_one']
        
        def create(self, validated_data):
            return ProductInOrder.objects.get_or_create(**validated_data)