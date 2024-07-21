from rest_framework import serializers
from apps.shop.models import CommentOfGoodsModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfGoodsModel
        fields = ["author","product","comment","time_comment"]

                        
        def create(self, validated_data):
            return CommentOfGoodsModel.objects.get_or_create(**validated_data)