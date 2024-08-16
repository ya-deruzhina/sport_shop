from apps.shop.models import SubCategoryModel, CategoryModel
from apps.shop.services import SubCategoryService

from faker import Faker
fake = Faker()

def get_subcategory_params(id_parent, subcategory):
    return {
        "subcategory": subcategory,
        "id_parent":id_parent,
    }


def perform(*args, **kwargs):
    parent = CategoryModel.objects.all()
    if len(SubCategoryModel.objects.all()) == 0:    
        for i in parent:
            subcategory = fake.first_name()
            SubCategoryService.create(get_subcategory_params(i.id, subcategory))
        