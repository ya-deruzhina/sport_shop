from ..models import RatingOfProductsModel
from ..serializers import RatingSerializer


class RatingService:
    model = RatingOfProductsModel

    @classmethod
    def create(cls, data):
        serializer = RatingSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



