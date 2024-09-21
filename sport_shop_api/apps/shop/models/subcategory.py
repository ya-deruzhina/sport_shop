from django.db import models
from apps.shop.models.category import CategoryModel


class SubCategoryModel (models.Model):
    id_parent = models.ForeignKey(to = CategoryModel, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length = 20, null=True)
    
    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return f'{self.subcategory}'
    