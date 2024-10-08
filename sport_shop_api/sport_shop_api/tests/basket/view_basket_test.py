from rest_framework.test import APIRequestFactory, APITestCase
from apps.shop.models import BasketModel
from apps.users.models import User 
from apps.shop.views import BasketView
from rest_framework import status
from rest_framework.test import force_authenticate

from sport_shop_api.tests.index import Index

# Test for BasketView (get)
class BasketViewTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    def test_only_view_basket_get(self):
        user = User.objects.all()[0]
        basket_first = BasketModel.objects.filter(user = user)
        request = APIRequestFactory().get('/api/v1/basket/')
        force_authenticate(request, user=user)
        response = BasketView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        item = response.data
        all_price = 0

        for basket in range (0,len(item)-1):
            assert  item['list'][0]['product'] == basket_first[basket].product.name
            assert  item['list'][0]['count'] == basket_first[basket].count
            assert  item['list'][0]['price_one'] == basket_first[basket].product.price
            sum_price = round((basket_first[basket].count * basket_first[basket].product.price),2)
            assert  item['list'][0]['price'] == sum_price

            all_price += sum_price
                                    
        self.assertEqual(item['all_price'], all_price)

    def test_only_view_basket_without_token_get(self):
        request = APIRequestFactory().get('/api/v1/basket/')
        response = BasketView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
