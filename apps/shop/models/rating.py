from django.db import models
from apps.users.models.user import User
from apps.shop.models.goods import GoodsModel
from django.utils.timezone import now


class RatingOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rating = models.IntegerField(null = False)
    # time_rating = models.DateTimeField(auto_now_add=True)
    time_rating = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.rating