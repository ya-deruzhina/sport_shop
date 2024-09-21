from django.db import models
from apps.users.models.user import User
from apps.shop.models.products import ProductsModel

class BasketModel (models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField (null=False)