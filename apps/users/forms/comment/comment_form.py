from django.forms import ModelForm
from apps.users.models import CommentOfGoodsModel

class CommentForm(ModelForm):
    class Meta:
        model = CommentOfGoodsModel
        fields = ["comment"]