from apps.shop.models import CategoryModel
from apps.shop.services import CategoryService

category = "Category"

def get_category_params():
    return {
        "category": category,
    }


def perform(*args, **kwargs):
    if not CategoryModel.objects.filter(category=category).exists():
        CategoryService.create(get_category_params())
    