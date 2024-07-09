from django.db import models
from apps.shop.models.category import CategoryModel, SubCategoryModel
from smart_selects.db_fields import ChainedForeignKey

class GoodsModel(models.Model):
    name = models.CharField(null = False, max_length = 100)
    description = models.TextField(null = False)
    price = models.FloatField(null = False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null = True)
    subcategory = ChainedForeignKey(
        SubCategoryModel,
        chained_field="category",
        chained_model_field="id_parent",
        show_all=False,
        auto_choose=True,
        sort=True,
        null = True)

    def __str__(self):
        return self.name