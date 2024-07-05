from django.db import models
from apps.users.models.user import User
from apps.shop.models.goods import GoodsModel


class RatingOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    rating = models.IntegerField(null = False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.rating