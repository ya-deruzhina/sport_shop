from apps.shop.models import ProductsModel, SubCategoryModel
from apps.shop.services import GoodsService

from faker import Faker
fake = Faker()

import random

def get_goods_params(category,subcategory):
    
    return {
        "name": fake.last_name(),
        "description": fake.sentence(),
        "price":random.randint(1, 50),
        "amount":random.randint(1, 10),
        "category":category,
        "subcategory":subcategory
    }



def perform(*args, **kwargs):
    subcategory = SubCategoryModel.objects.all()
    if len(ProductsModel.objects.all()) == 0:
        for i in subcategory:
            if not ProductsModel.objects.filter(category = i.id_parent.id, subcategory = i.id).exists():
                GoodsService.create(get_goods_params(i.id_parent.id, i.id))

      