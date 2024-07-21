from ..models import BasketModel
from ..serializers import BasketSerializer


class BasketService:
    model = BasketModel

    @classmethod
    def create(cls, data):
        serializer = BasketSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



