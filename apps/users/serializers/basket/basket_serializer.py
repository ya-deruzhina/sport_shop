from rest_framework import serializers
from apps.users.models import BasketModel

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = ['user','product','count']
        
        def create(self, validated_data):
            return BasketModel.objects.create(**validated_data)