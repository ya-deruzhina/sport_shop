from rest_framework import serializers
from apps.shop.models import CommentOfProductsModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfProductsModel
        fields = ["author","product","comment","time_comment"]

                        
        def create(self, validated_data):
            return CommentOfProductsModel.objects.get_or_create(**validated_data)