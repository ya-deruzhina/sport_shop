from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shop.models import BasketModel, ProductsModel
from apps.shop.serializers import BasketSerializer
from apps.shop.views.basket.basket_servese import BaskerServiseView

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
    def post (self, request, product_id):
        user_id = request.user.id
        product_for_user = BasketModel.objects.filter(product=product_id)

        try:
            users_with_product = product_for_user.get(user=user_id)
        
        except:
            basket = {'user':user_id,'product':product_id,'count':1}
            try:
                serializer = BasketSerializer(data=basket)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        
            except Exception as exs:
                return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            users_with_product.count += 1
            users_with_product.save()
            serializer = BasketSerializer(instance=users_with_product)

        try:
            catalog_amount = ProductsModel.objects.get(id=product_id)
            if catalog_amount.amount == 0:
                return HttpResponseRedirect ("/api/v1/404_error/")
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()

        except Exception as exs:
                return HttpResponseRedirect ("/api/v1/404_error/")

        # return HttpResponseRedirect ("/api/v1/basket/")
        return Response ({"information":serializer.data})     
    