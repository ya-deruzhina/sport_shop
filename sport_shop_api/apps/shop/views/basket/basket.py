from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shop.models import BasketModel
from apps.shop.views.basket.basket_servise import BaskerServiseView

from core import IsActive

class BasketView(APIView):
    permission_classes = (IsActive,)
    
    # Page of Basket
    def get(self,request, **kwargs):
        id_user = request.user.id
        user_basket = BasketModel.objects.filter(user_id=id_user).order_by('product_id')
        basket_with_price = BaskerServiseView.basket_service(user_basket)

        return Response (basket_with_price)

    
    # Add Product to Basket
    def post (self, request, ** kwargs):
        user_id = request.user.id
        if 'basket_id' in kwargs.keys():
            try:
                product_id = BasketModel.objects.get(id=kwargs['basket_id']).product.id
            except:
                return HttpResponseRedirect ("/api/v1/404_error/")
        else:
            product_id = kwargs['product_id']

        add_basket = BaskerServiseView.add_basket_service(user_id, product_id)

        return HttpResponseRedirect ("/api/v1/basket/")
  
    