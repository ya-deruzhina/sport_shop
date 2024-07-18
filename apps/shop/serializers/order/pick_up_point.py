from rest_framework import serializers
from apps.shop.models import PickUpModel


class PickUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickUpModel
        fields = ['adres','description ']