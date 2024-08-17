from ..models import ProductsModel
from ..serializers import CatalogSerializer


class GoodsService:
    model = ProductsModel

    @classmethod
    def create(cls, data):
        serializer = CatalogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



