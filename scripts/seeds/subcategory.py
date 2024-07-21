from apps.shop.models import SubCategoryModel, CategoryModel
from apps.shop.services import SubCategoryService

subcategory = "SubCategory"
id_parent = CategoryModel.objects.all()[0].id

def get_subcategory_params():
    return {
        "subcategory": subcategory,
        "id_parent":id_parent,
    }


def perform(*args, **kwargs):
    if not SubCategoryModel.objects.filter(subcategory=subcategory).exists():
        SubCategoryService.create(get_subcategory_params())
    