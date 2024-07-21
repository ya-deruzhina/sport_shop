from apps.shop.models import GoodsModel
from apps.users.models import User
from apps.shop.services import RatingService

import random


author = User.objects.all()[0].id
product = GoodsModel.objects.all()[0].id

def get_rating_params():
    return {
        "author": author,
        "product":product,
        "rating":random.randint(1, 5)
    }



def perform(*args, **kwargs):
    RatingService.create(get_rating_params())
    