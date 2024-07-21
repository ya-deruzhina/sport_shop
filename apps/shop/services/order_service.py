from ..models import OrderModel
from ..serializers import OrderSerializer


class OrderService:
    model = OrderModel

    @classmethod
    def create(cls, data):
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



