from apps.shop.models import GoodsModel
from apps.users.models import User
from apps.shop.services import BasketService
import random

user = User.objects.all()[0].id
product = GoodsModel.objects.all()[0].id

def get_comment_params():
    return {
        "user": user,
        "product":product,
        "count":random.randint(1, 5)
    }



def perform(*args, **kwargs):
    BasketService.create(get_comment_params())
    
