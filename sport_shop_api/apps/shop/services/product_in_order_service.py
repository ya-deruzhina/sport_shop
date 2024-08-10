from ..models import ProductInOrder
from ..serializers import OrderProductSerializer


class ProductInOrderService:
    model = ProductInOrder

    @classmethod
    def create(cls, data):
        serializer = OrderProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



