from rest_framework.test import APIRequestFactory, APITestCase
from apps.shop.models import OrderModel
from apps.users.models import User
from apps.shop.views import OneOrdersUserView
from rest_framework.test import force_authenticate

from sport_shop_api.tests.index import Index

# Test for One Order (get)
class OneOrderTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    def test_one_correct_order_get(self):
        user = User.objects.all()[0]
        order_id = OrderModel.objects.all()[0].id
        
        request = APIRequestFactory().get('/api/v1/order/')
        force_authenticate(request, user=user)
        response = OneOrdersUserView.as_view()(request,order_id = order_id)

        assert response.status_code == 200


    def test_one_order_get(self):
        user = User.objects.all()[0]
        order_id = 999999999999999999999999
        
        request = APIRequestFactory().get('/api/v1/order/')
        force_authenticate(request, user=user)
        response = OneOrdersUserView.as_view()(request,order_id = order_id)
        assert response.data.status_code== 302