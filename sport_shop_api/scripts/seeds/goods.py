from apps.shop.models import GoodsModel, SubCategoryModel, CategoryModel
from apps.users.models import User
from apps.shop.services import GoodsService
from apps.shop.serializers import CategorySerializer, SubCategorySerializer

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
    if len(GoodsModel.objects.all()) == 0:
        for i in subcategory:
            if not GoodsModel.objects.filter(category = i.id_parent.id, subcategory = i.id).exists():
                GoodsService.create(get_goods_params(i.id_parent.id, i.id))

      