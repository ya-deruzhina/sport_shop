from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from apps.users.models import BasketModel, User, GoodsModel
from apps.users.serializers import BasketSerializer
from apps.users.forms import CreateOrderForm


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening


class BasketAddView(APIView):
    permission_classes = [IsAuthenticated]
    # Добавляет 1 шт в корзину
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except Exception  as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            basket.count +=1


        try:
            catalog_amount = GoodsModel.objects.get(id=basket.product_id)
            if catalog_amount.amount == 0:
                template = loader.get_template("catalog/error_not_product.html")
                return HttpResponse(template.render())
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()
            
        except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
        
        basket.save()

        return HttpResponseRedirect ("/basket/")