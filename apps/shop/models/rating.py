from django.db import models
from apps.users.models.user import User
from apps.shop.models.goods import GoodsModel
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rating = models.IntegerField(null = False,validators=[MinValueValidator(0), MaxValueValidator(5)])
    time_rating = models.DateTimeField(auto_now_add=True, null = True)

    def __int__(self):
        return self.rating