from django.http import HttpResponseRedirect
from apps.shop.serializers import BasketSerializer
from apps.shop.models import BasketModel, ProductsModel

class BaskerServiseView:

    def basket_service(func):
        basket_with_price = {}
        basket_list = []
        all_price = 0

        for basket in range (0,len(func)):
            baskets ={}
            baskets['product'] = func[basket].product.name
            baskets['count'] = func[basket].count
            baskets['price_one'] = func[basket].product.price

            baskets['price'] = round((baskets['count'] * baskets['price_one']),2)
            all_price += baskets['price']
                                    
            baskets['id'] = func[basket].id
            basket_list.append(baskets)
        
        basket_with_price['list'] = basket_list
        basket_with_price['all_price'] = (round(all_price,2))
        return basket_with_price
    
    def add_basket_service (user_id,product_id):
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

        try:
            catalog_amount = ProductsModel.objects.get(id=product_id)
            if catalog_amount.amount == 0:
                return HttpResponseRedirect ("/api/v1/404_error/")
            else:
                catalog_amount.amount -= 1
                catalog_amount.save()

        except Exception as exs:
                return HttpResponseRedirect ("/api/v1/404_error/")
        
    def delete_basket_service (user_id, product_id):

        try:
            product_for_user = BasketModel.objects.filter(product=product_id)
            basket = product_for_user.get(user=user_id)

        except:
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            basket.count -=1
        
            if basket.count == 0:
                basket.delete()
                return HttpResponseRedirect ("/api/v1/basket/")
            
            try:
                catalog_amount = ProductsModel.objects.get(id=product_id)
                catalog_amount.amount += 1
                catalog_amount.save()
                
            except Exception:
                return HttpResponseRedirect ("/api/v1/404_error/")
        
        basket.save()