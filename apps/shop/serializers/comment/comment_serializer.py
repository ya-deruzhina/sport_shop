from rest_framework import serializers
from apps.shop.models import CommentOfGoodsModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfGoodsModel
        fields = ["author","product","comment","time_comment"]