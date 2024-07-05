from rest_framework import serializers
from apps.shop.models import GoodsModel

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsModel
        fields = ["id","name","description","price","id_parent"]