from django.forms import ModelForm
from apps.shop.models import CommentOfGoodsModel

class CommentForm(ModelForm):
    class Meta:
        model = CommentOfGoodsModel
        fields = ["comment"]