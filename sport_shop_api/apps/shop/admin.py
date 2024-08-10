from django.contrib import admin
from apps.shop.models import *
from apps.users.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

# Register your models here.

admin.site.register(PickUpModel)


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
    fields = ["name","description","price","amount","category","subcategory"]
    inlines = [CommentInline,RatingInline]
    list_display = ["name","category","subcategory","price"]
    list_filter = ["category","subcategory"]

class ProductInOrderInline (admin.TabularInline):
    model = ProductInOrder
    fields = ["product", "count", "price_one"]
    ordering = ["-id"]

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

class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ('pick_up_point','date_of_pick_up','time_of_pick_up')

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        if len(OrderModel.objects.filter(pick_up_point = cleaned_data.get("pick_up_point")).filter(date_of_pick_up=cleaned_data.get("date_of_pick_up")).filter(time_of_pick_up=cleaned_data.get("time_of_pick_up"))) >= 5:
            raise ValidationError
        return cleaned_data

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    inlines = [ProductInOrderInline]
    date_hierarchy = 'order_time'
    list_display = ["user","order_time","pick_up_point","date_of_pick_up","time_of_pick_up","comment"]
    list_filter = ["user__username","pick_up_point__adres","date_of_pick_up","time_of_pick_up"]
