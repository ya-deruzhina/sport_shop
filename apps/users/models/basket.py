from django.db import models
from apps.users.models.user import User
from apps.users.models.goods import GoodsModel

class BasketModel (models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(GoodsModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField (null=False)