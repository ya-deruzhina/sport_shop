from apps.shop.models import GoodsModel, BasketModel
from apps.users.models import User
from apps.shop.services import BasketService
import random

def get_basket_params(user, product):
    return {
        "user": user,
        "product":product,
        "count":random.randint(1, 5)
    }


def perform(*args, **kwargs):
    user = User.objects.all()
    product = GoodsModel.objects.all()
    if len(BasketModel.objects.all()) == 0:
        for i in user:
            for m in product:
                if not BasketModel.objects.filter(product = m.id, user = i.id).exists():
                    BasketService.create(get_basket_params(i.id, m.id))
    
