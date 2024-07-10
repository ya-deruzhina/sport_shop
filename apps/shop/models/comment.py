from django.db import models
from apps.users.models.user import User
from apps.shop.models.goods import GoodsModel
from django.utils.timezone import now
# from settings import ADMIN_DATE_FORMATS


class CommentOfGoodsModel (models.Model):
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null = False)
    time_comment = models.DateTimeField(auto_now_add=True)