from rest_framework import serializers
from apps.shop.models import RatingOfGoodsModel

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingOfGoodsModel
        fields = ["author","rating","comment"]