from django.db import models

class CategoryModel (models.Model):
    category = models.CharField(max_length = 20, null=True)
    
    def __str__(self):
        return self.category


class SubCategoryModel (models.Model):
    id_parent = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length = 20, null=True)

    def __str__(self):
        return self.subcategory
    