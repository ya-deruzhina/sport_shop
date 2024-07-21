from ..models import GoodsModel
from ..serializers import CatalogSerializer


class GoodsService:
    model = GoodsModel

    @classmethod
    def create(cls, data):
        serializer = CatalogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



