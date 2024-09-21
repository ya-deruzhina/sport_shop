from django.db import models

class CategoryModel (models.Model):
    category = models.CharField(max_length = 20, null=True)
    def __str__(self):
        return f'{self.category}'
    