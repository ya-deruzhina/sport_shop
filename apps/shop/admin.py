from django.contrib import admin
from apps.shop.models import *

# Register your models here.

admin.site.register(BasketModel)
admin.site.register(CommentOfGoodsModel)
admin.site.register(GoodsModel)
admin.site.register(OrderModel)
admin.site.register(PickUpModel)
admin.site.register(ProductInOrder)
admin.site.register(RatingOfGoodsModel)
admin.site.register(TegsOfGoodsModel)