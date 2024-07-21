from rest_framework import serializers
from apps.shop.models import PickUpModel


class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpModel
        fields = ['adres','description']

                        
        def create(self, validated_data):
            return PickUpModel.objects.get_or_create(**validated_data)