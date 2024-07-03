from django.db import models
from apps.users.models.user import User
from apps.users.models.pick_up_point import PickUpModel


class OrderModel(models.Model):    
    order_time = models.DateTimeField(auto_now_add = True, null = True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(null = False,max_length = 100)
    phone = models.BigIntegerField(null = False)
    pick_up_point = models.ForeignKey(PickUpModel, null=False, on_delete=models.CASCADE)
    date_of_pick_up = models.DateField()
    comment = models.TextField(null = True, default = 'Order without Comment')
    total_money = models.FloatField(null=False)

    
