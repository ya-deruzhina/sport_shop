from django.db import models
from apps.users.models.user import User
from apps.shop.models.goods import GoodsModel

class CommentOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null = False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment