from ..models import CommentOfProductsModel
from ..serializers import CommentSerializer


class CommentService:
    model = CommentOfProductsModel

    @classmethod
    def create(cls, data):
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



