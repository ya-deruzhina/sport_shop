from apps.shop.models import CategoryModel
from apps.shop.services import CategoryService

from faker import Faker
fake = Faker()

def get_category_params(category):
    return {
        "category": category,
    }


def perform(*args, **kwargs):
    category = fake.first_name()
    if len(CategoryModel.objects.all())==0:
        CategoryService.create(get_category_params(category))
    