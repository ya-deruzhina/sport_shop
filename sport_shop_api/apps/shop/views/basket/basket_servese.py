from rest_framework.response import Response

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