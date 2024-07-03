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


class BasketView(APIView):
    # Страница корзины

    def get(self,request, **kwargs):
        id_user = request.user.id
        user_basket = BasketModel.objects.filter(user_id=id_user).order_by('product_id')
        basket_with_price = {}
        all_price = 0
        price_without_discont = 0

        # for basket in range (0,len(user_basket)):
        #     baskets ={}
        #     baskets['pizza'] = user_basket[basket].pizza.name_pizza
        #     baskets['count'] = user_basket[basket].count
        #     baskets['one_price_without_discont'] = user_basket[basket].pizza.price
        #     user_discont = User.objects.get(id = id_user).discont
            
        #     if user_basket[basket].pizza.price_disсont !=0:
        #         baskets['price_one'] = user_basket[basket].pizza.price_disсont
        #     else:
        #         if user_discont != 0:
        #             baskets['price_one'] = round(user_basket[basket].pizza.price * (1-(user_discont/100)), 2)
        #         else:
        #             baskets['price_one'] = user_basket[basket].pizza.price

        #     baskets['price'] = round((baskets['count'] * baskets['price_one']),2)
        #     all_price += baskets['price']
            
        #     baskets ['basket_without_discont'] = baskets['count'] * baskets['one_price_without_discont']
        #     price_without_discont += baskets ['basket_without_discont']
                        
        #     baskets['id'] = user_basket[basket].id
        #     basket_with_price[basket] = baskets
        
        # discont = round((price_without_discont - all_price),2)
        # price_without_discont = round(price_without_discont,2)
        # all_price = round(all_price,2)

        # keys = basket_with_price.keys()
        context = {
            "basket_with_price":basket_with_price,
            "form":CreateOrderForm(),
            # "keys":keys,
            "all_price": all_price,
            # "discont":discont,
            "price_without_discont":price_without_discont,
        }
        if all_price != price_without_discont:
            template = loader.get_template("basket/basket_with_discont.html")
        else:
            template = loader.get_template("basket/basket.html")

        return HttpResponse(template.render(context,request))
    
    def post (self, request, product_id):
        user_id = request.user.id
        pizza_for_user = BasketModel.objects.filter(product=product_id)

        try:
            users_with_pizza = pizza_for_user.get(user=user_id)
        except:
            basket = {'user':user_id,'product':product_id,'count':1}
            try:
                serializer = BasketSerializer(data=basket)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        
            except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())
        
        else:
            users_with_pizza.count += 1
            users_with_pizza.save()

        try:
            catalog_amount = GoodsModel.objects.get(id=product_id)
            if catalog_amount.amount == 0:
                template = loader.get_template("catalog/error_not_pizza.html")
                return HttpResponse(template.render())
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()

        except Exception as exs:
                print ('Warming!!!', exs)   
                template = loader.get_template("main/page_404.html")
                return HttpResponse(template.render())

        return HttpResponseRedirect ("/basket/") 
    
