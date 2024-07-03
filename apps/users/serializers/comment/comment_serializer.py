from rest_framework import serializers
from apps.users.models import CommentOfGoodsModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfGoodsModel
        fields = ["author","product","comment"]