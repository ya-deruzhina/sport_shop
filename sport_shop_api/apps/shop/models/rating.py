from django.db import models
from apps.users.models.user import User
from apps.shop.models.products import ProductsModel
from django.core.validators import MinValueValidator, MaxValueValidator


class RatingOfProductsModel (models.Model):
    product = models.ForeignKey(ProductsModel, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rating = models.IntegerField(null = False,validators=[MinValueValidator(0), MaxValueValidator(5)])
    time_rating = models.DateTimeField(auto_now_add=True, null = True)

    def __int__(self):
        return self.rating