from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


from apps.shop.models import BasketModel, GoodsModel



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening


class BasketAddView(APIView):
    permission_classes = [IsAuthenticated]
    # Add to basket
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except:
            return HttpResponseRedirect ("/404_error/")
        
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

        return HttpResponseRedirect ("/basket/")