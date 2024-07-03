from rest_framework import serializers
from apps.users.models import RatingOfGoodsModel

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingOfGoodsModel
        fields = ["author","rating","comment"]