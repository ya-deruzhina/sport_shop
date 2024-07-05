from django.forms import ModelForm
from apps.shop.models import OrderModel

class CreateOrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ["comment"]