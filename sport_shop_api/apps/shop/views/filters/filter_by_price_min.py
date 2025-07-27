from apps.shop.models import GoodsModel
from apps.shop.serializers import CatalogSerializer

from rest_framework import generics
from rest_framework import viewsets

class FilterPriceMinView(generics.ListCreateAPIView):
    queryset = GoodsModel.objects.all().order_by('price')
    serializer_class = CatalogSerializer