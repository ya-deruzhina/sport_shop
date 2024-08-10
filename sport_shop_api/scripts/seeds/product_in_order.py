from apps.shop.models import OrderModel, GoodsModel, ProductInOrder
from apps.shop.services import ProductInOrderService

from faker import Faker
fake = Faker()

import random

def get_order_params(order, product):
    return {
        "order": order,
        "product":product,
        "count":random.randint(1, 10),
        "price_one":random.randint(1, 50),
    }


def perform(*args, **kwargs):
    product = GoodsModel.objects.all()
    order = OrderModel.objects.all()
    for i in order:
        for m in product:
            if not ProductInOrder.objects.filter(product = m.id, order = i.id).exists():
                ProductInOrderService.create(get_order_params(i.id, m.id))