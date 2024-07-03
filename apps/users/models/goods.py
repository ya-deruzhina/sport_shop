from django.db import models

class GoodsModel(models.Model):
    name = models.CharField(null = False, max_length = 100)
    description = models.TextField(null = False)
    price = models.FloatField(null = False)
    id_parent = models.IntegerField()

    def __str__(self):
        return self.name