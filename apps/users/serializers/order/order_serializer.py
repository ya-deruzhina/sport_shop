from rest_framework import serializers
from apps.users.models import OrderModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['user','name','phone','comment',"total_money"]
        
        def create(self, validated_data):
            return OrderModel.objects.create(**validated_data)