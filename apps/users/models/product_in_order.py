from django.db import models
from apps.users.models.order import OrderModel
from apps.users.models.goods import GoodsModel

class ProductInOrder (models.Model):
    order = models.ForeignKey(OrderModel, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey (GoodsModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField()
    price_one = models.FloatField(null = False)

    def serilize_from_db (self):
        return {'id':self.id, 'order':self.order,'product':self.product,'count':self.count,'price_one':self.price_one}

