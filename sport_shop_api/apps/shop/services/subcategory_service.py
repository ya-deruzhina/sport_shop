from ..models import SubCategoryModel
from ..serializers import SubCategorySerializer


class SubCategoryService:
    model = SubCategoryModel

    @classmethod
    def create(cls, data):
        serializer = SubCategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data



