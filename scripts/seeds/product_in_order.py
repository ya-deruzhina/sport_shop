from apps.shop.models import OrderModel, GoodsModel
from apps.shop.services import ProductInOrderService

from faker import Faker
fake = Faker()

import random

product = GoodsModel.objects.all()[0].id
order = OrderModel.objects.all()[0].id


def get_order_params():
    return {
        "order": order,
        "product":product,
        "count":random.randint(1, 10),
        "price_one":random.randint(1, 50),
    }



def perform(*args, **kwargs):
    ProductInOrderService.create(get_order_params())
