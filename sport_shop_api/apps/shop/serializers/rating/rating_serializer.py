from rest_framework import serializers
from apps.shop.models import RatingOfProductsModel

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingOfProductsModel
        fields = ["author","product","rating"]

                        
        def create(self, validated_data):
            return RatingOfProductsModel.objects.create(**validated_data)