from ..models import PickUpModel
from ..serializers import PickUpSerializer


class PickUpService:
    model = PickUpModel

    @classmethod
    def create(cls, data):
        serializer = PickUpSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



