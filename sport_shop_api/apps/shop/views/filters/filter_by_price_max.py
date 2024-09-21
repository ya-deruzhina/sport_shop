from apps.shop.models import ProductsModel
from apps.shop.serializers import CatalogSerializer

from rest_framework import viewsets
from rest_framework import generics

class FilterPriceMaxView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all().order_by('-price')
    serializer_class = CatalogSerializer