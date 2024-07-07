from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response 

from apps.shop.serializers import BasketSerializer
from apps.shop.models import BasketModel, GoodsModel

from core import IsActive


class BasketAddView(APIView):
    permission_classes = (IsActive,)
    # Add to basket
    def post (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except:
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            basket.count +=1
        

    # !!!! Остаток в наличии
        # try:
        #     catalog_amount = GoodsModel.objects.get(id=basket.product_id)
        #     if catalog_amount.amount == 0:
        #         template = loader.get_template("catalog/error_not_product.html")
        #         return HttpResponse(template.render())
        #     else:
        #         catalog_amount.amount -= 1
        #         catalog_amount.save()
            
        # except:
        #     return HttpResponseRedirect ("/404_error/")
        
        basket.save()
        serializer = BasketSerializer(instance=basket)

        # return HttpResponseRedirect ("/basket/")
        return Response ({"information":serializer.data}) 


    

  
  
