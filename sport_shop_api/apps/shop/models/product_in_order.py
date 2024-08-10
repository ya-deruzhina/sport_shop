from django.db import models
from apps.shop.models.order import OrderModel
from apps.shop.models.goods import GoodsModel

class ProductInOrder (models.Model):
    order = models.ForeignKey(OrderModel, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey (GoodsModel, null=False, on_delete=models.CASCADE)
    count = models.IntegerField()
    price_one = models.DecimalField(max_digits=10, decimal_places=2,null = False)

    def serilize_from_db (self):
        return {'id':self.id, 'order':self.order,'product':self.product,'count':self.count,'price_one':self.price_one}

