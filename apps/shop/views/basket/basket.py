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


class BasketView(APIView):
    # Страница корзины

    def get(self,request, **kwargs):
        id_user = request.user.id
        user_basket = BasketModel.objects.filter(user_id=id_user).order_by('product_id')
        basket_with_price = {}
        all_price = 0

        for basket in range (0,len(user_basket)):
            baskets ={}
            baskets['product'] = user_basket[basket].product.name
            baskets['count'] = user_basket[basket].count
            baskets['price_one'] = user_basket[basket].product.price

            baskets['price'] = round((baskets['count'] * baskets['price_one']),2)
            all_price += baskets['price']
                                    
            baskets['id'] = user_basket[basket].id
            basket_with_price[basket] = baskets
        
        all_price = round(all_price,2)

        keys = basket_with_price.keys()
        context = {
            "basket_with_price":basket_with_price,
            "form":CreateOrderForm(),
            "keys":keys,
            "all_price": all_price,
        }
        
        template = loader.get_template("basket/basket.html")

        return HttpResponse(template.render(context,request))
    
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
                return HttpResponseRedirect ("/404_error/")
        
        else:
            users_with_product.count += 1
            users_with_product.save()

        # !!!!!! Amount
        # try:
        #     catalog_amount = GoodsModel.objects.get(id=product_id)
        #     if catalog_amount.amount == 0:
        #         template = loader.get_template("catalog/error_not_pizza.html")
        #         return HttpResponse(template.render())
        #     else:
        #         catalog_amount.amount -= 1
        #         catalog_amount.save()

        # except Exception as exs:
        #         return HttpResponseRedirect ("/404_error/")

        return HttpResponseRedirect ("/basket/") 
    
