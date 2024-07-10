from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate

from apps.shop.models import BasketModel, GoodsModel
from apps.users.models import User
from apps.shop.views import BasketDeleteView


class BasketDeleteViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_basket_get(self):
        user = User.objects.all()[0]
        basket = BasketModel.objects.all()
        basket_id = basket[0].id
        basket_count_first = basket[0].count
        amount = GoodsModel.objects.exclude(amount = 0)[0]
        amount_id = amount.id
        first_amount = GoodsModel.objects.get(id=amount_id).amount

        request = APIRequestFactory().get('/api/v1/basket/delete/')
        force_authenticate(request, user=user)
        response = BasketDeleteView.as_view()(request,basket_id = basket_id)

        assert response.status_code == 200
        basket = BasketModel.objects.get(id = basket_id)
    
        item = response.data

        self.assertEqual(item['information']['user'], basket.user.id)
        self.assertEqual(item['information']['product'], basket.product.id)

        assert (basket_count_first - 1 == basket.count)
        assert (first_amount + 1) == GoodsModel.objects.get(id=amount_id).amount 
 

    def test_delete_basket_false_id_get(self):
        user = User.objects.all()[0]
        basket_id = 999999999999999999999999999999999

        request = APIRequestFactory().get('/api/v1/basket/delete/')
        force_authenticate(request, user=user)
        response = BasketDeleteView.as_view()(request,basket_id = basket_id)
        assert response.status_code == 302