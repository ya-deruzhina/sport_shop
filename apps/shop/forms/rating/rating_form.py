from django.forms import ModelForm
from apps.shop.models import RatingOfGoodsModel

class RatingForm(ModelForm):
    class Meta:
        model = RatingOfGoodsModel
        fields = ["rating"]