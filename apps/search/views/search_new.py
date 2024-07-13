from django.contrib.auth.models import User
from rest_framework import viewsets

from apps.shop.models import GoodsModel
from apps.shop.serializers import CatalogSerializer


class CatalogSearchViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = GoodsModel.objects.all()

