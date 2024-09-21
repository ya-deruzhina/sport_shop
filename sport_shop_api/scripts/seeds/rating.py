from apps.shop.models import ProductsModel, RatingOfProductsModel
from apps.users.models import User
from apps.shop.services import RatingService

import random

def get_rating_params(author, product):
    return {
        "author": author,
        "product":product,
        "rating":random.randint(1, 5)
    }



def perform(*args, **kwargs):
    goods = ProductsModel.objects.all()
    author = User.objects.all()
    if len (RatingOfProductsModel.objects.all()) == 0:
        for i in goods:
            for m in author:
                if not RatingOfProductsModel.objects.filter(product = i.id, author = m.id).exists():
                    RatingService.create(get_rating_params(m.id, i.id))