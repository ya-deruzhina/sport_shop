from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from apps.users.models import User
from apps.shop.models import BasketModel, GoodsModel
from apps.shop.serializers import BasketSerializer
from apps.shop.forms import CreateOrderForm


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening


class BasketDelete(APIView):
    permission_classes = [IsAuthenticated]
    # Удаляет 1 шт из корзины - при 0 шт удаляет запись из БД
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)
            
        except Exception  as exs:
            return HttpResponseRedirect ("/404_error/")
        
        else:
            basket.count -=1
            basket.save()
            # !!!!! Добавить остаток в наличии
            # if basket.count == 0:
            #     basket.delete()
            
            # try:
            #     catalog_amount = GoodsModel.objects.get(id=basket.product_id)
            #     catalog_amount.amount += 1
            #     catalog_amount.save()
                
            # except Exception as exs:
            #         return HttpResponseRedirect ("/404_error/")
    
        return HttpResponseRedirect ("/basket/")
    


    