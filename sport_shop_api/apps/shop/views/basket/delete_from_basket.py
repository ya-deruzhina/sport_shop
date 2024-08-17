from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from apps.users.models import User
from apps.shop.models import BasketModel, ProductsModel
from apps.shop.serializers import BasketSerializer



from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response 

from apps.shop.serializers import BasketSerializer
from apps.shop.models import BasketModel, ProductsModel

from core import IsActive

class BasketDeleteView(APIView):
    permission_classes = (IsActive,)
    # Delete from basket
    def get (self,request, basket_id):
        try:
            basket = BasketModel.objects.get(id=basket_id)

        except:
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            basket.count -=1
        
            if basket.count == 0:
                basket.delete()
                return HttpResponseRedirect ("/api/v1/basket/")
            
            try:
                catalog_amount = ProductsModel.objects.get(id=basket.product_id)
                catalog_amount.amount += 1
                catalog_amount.save()
                
            except Exception:
                return HttpResponseRedirect ("/api/v1/404_error/")
        
        basket.save()
        serializer = BasketSerializer(instance=basket)

        # return HttpResponseRedirect ("/basket/")
        return Response ({"information":serializer.data}) 


    

  
  
