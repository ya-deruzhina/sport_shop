from django.db import models
from apps.shop.models.category import CategoryModel, SubCategoryModel
from smart_selects.db_fields import ChainedForeignKey

class GoodsModel(models.Model):
    name = models.CharField(null = False, max_length = 100)
    description = models.TextField(null = False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null = False)
    amount = models.IntegerField(default = 0)
    category = models.ForeignKey(to = CategoryModel, on_delete=models.CASCADE, null = True,related_name='categories')
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