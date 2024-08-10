from ..models import CommentOfGoodsModel
from ..serializers import CommentSerializer


class CommentService:
    model = CommentOfGoodsModel

    @classmethod
    def create(cls, data):
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



