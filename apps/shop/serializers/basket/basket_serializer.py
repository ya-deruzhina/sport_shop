from rest_framework import serializers
from apps.shop.models import BasketModel

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = ['id','user','product','count']
        
        def create(self, validated_data):
            return BasketModel.objects.get_or_create(**validated_data)