from django.db import models
from apps.users.models.user import User
from apps.shop.models.products import ProductsModel


class CommentOfProductsModel (models.Model):
    product = models.ForeignKey(ProductsModel, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null = False)
    time_comment = models.DateTimeField(auto_now_add=True)