from django.http import HttpResponseRedirect

from rest_framework.views import APIView

from apps.shop.models import BasketModel
from apps.shop.views.basket.basket_servise import BaskerServiseView

from core import IsActive

class BasketDeleteView(APIView):
    permission_classes = (IsActive,)
    
    # Delete from basket
    def get (self,request, **kwargs):
        user_id = request.user.id
        
        if 'basket_id' in kwargs.keys():
            product_id = BasketModel.objects.get(id=kwargs['basket_id']).product.id
        else:
            product_id = kwargs['product_id']

        add_basket = BaskerServiseView.delete_basket_service(user_id, product_id)

        return HttpResponseRedirect ("/api/v1/basket/")


    

  
  
