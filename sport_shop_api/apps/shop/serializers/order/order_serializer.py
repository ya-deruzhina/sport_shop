from rest_framework import serializers
from apps.shop.models import OrderModel

from apps.shop.serializers.order.pick_up_point import PickUpSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel    
        fields = ['id','user','name','email','comment','pick_up_point','date_of_pick_up','time_of_pick_up','total_money']
        
        def create(self, validated_data):
            return OrderModel.objects.get_or_create(**validated_data)