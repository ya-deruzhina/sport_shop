from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate

from apps.shop.models import BasketModel
from apps.users.models import User
from apps.shop.views import BasketAddView


class BasketAddFromBasketTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_add_view_basket_post(self):
        user = User.objects.all()[0]
        basket = BasketModel.objects.all()
        basket_id = basket[0].id
        basket_count_first = basket[0].count
        # amount = CatalogModel.objects.exclude(amount = 0)[0]
        # amount_id = amount.id
        # first_amount = GoodsModel.objects.get(id=amount_id).amount

        request = APIRequestFactory().post('/api/v1/basket/add/')
        force_authenticate(request, user=user)
        response = BasketAddView.as_view()(request,basket_id = basket_id)

        assert response.status_code == 200
        basket = BasketModel.objects.get(id = basket_id)
    
        item = response.data

        self.assertEqual(item['information']['user'], basket.user.id)
        self.assertEqual(item['information']['product'], basket.product.id)

        assert (basket_count_first + 1 == basket.count) 

    def test_add_view_basket_false_id_post(self):
        user = User.objects.all()[0]
        basket_id = 999999999999999999999999999999999

        request = APIRequestFactory().post('/api/v1/basket/add/')
        force_authenticate(request, user=user)
        response = BasketAddView.as_view()(request,basket_id = basket_id)
        assert response.status_code == 302
