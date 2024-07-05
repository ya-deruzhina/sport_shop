from django.db import models
from apps.shop.models.goods import GoodsModel

class TegsOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    teg = models.TextField(null = False)

    def __str__(self):
        return self.teg