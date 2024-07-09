from django.contrib import admin
from apps.shop.models import *
from apps.users.models import User

# Register your models here.

admin.site.register(PickUpModel)
admin.site.register(TegsOfGoodsModel)


class CommentInline(admin.TabularInline):
    model = CommentOfGoodsModel
    lfields = ["author", "comment"]
    ordering = ["-id"]

class RatingInline(admin.TabularInline):
    model = RatingOfGoodsModel
    fields = ["author", "rating"]
    ordering = ["-id"]

@admin.register(GoodsModel)
class GoodsModelAdmin (admin.ModelAdmin):
    fields = ["name","description","price","category","subcategory"]
    inlines = [CommentInline,RatingInline]
    list_display = ["name","category","subcategory","price"]
    list_filter = ["category","subcategory"]

class ProductInOrderInline (admin.TabularInline):
    model = ProductInOrder
    fields = ["product", "count", "price_one"]
    ordering = ["-id"]

@admin.register(OrderModel)
class OrderModelAdmin (admin.ModelAdmin):
    inlines = [ProductInOrderInline]
    date_hierarchy = 'order_time'
    list_display = ["user","order_time","pick_up_point","date_of_pick_up","time_of_pick_up","comment"]
    list_filter = ["user__username","pick_up_point__adres","time_of_pick_up"]

class SubCategoryInOrderInline (admin.TabularInline):
    model = SubCategoryModel
    fields = ["subcategory"]
    ordering = ["-id"]

@admin.register(CategoryModel)
class CategoryModelAdmin (admin.ModelAdmin):
    fields = ["category"]
    inlines = [SubCategoryInOrderInline]
    ordering = ["-id"]

class BasketInOrderInline (admin.TabularInline):
    model = BasketModel
    fields = ["product","count"]
    ordering = ["-id"]

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    fields = ["username","email","first_name","last_name","status","role","last_login"]
    inlines = [BasketInOrderInline]
    ordering = ["-username"]



