from apps.shop.models import GoodsModel, RatingOfGoodsModel
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
    goods = GoodsModel.objects.all()
    author = User.objects.all()
    for i in goods:
        for m in author:
            if not RatingOfGoodsModel.objects.filter(product = i.id, author = m.id).exists():
                RatingService.create(get_rating_params(m.id, i.id))
    