from rest_framework import serializers
from apps.shop.models import RatingOfGoodsModel

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingOfGoodsModel
        fields = ["author","product","rating"]

                        
        def create(self, validated_data):
            return RatingOfGoodsModel.objects.create(**validated_data)