from rest_framework.test import APIRequestFactory, APITestCase
from apps.shop.models import OrderModel
from apps.users.models import User
from apps.shop.views import OrderView
from rest_framework import status
from rest_framework.test import force_authenticate

from sport_shop_api.tests.index import Index

        
class OrderViewTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    # Test for OrderView (get)
    def test_order_view_true_get(self):
        user = User.objects.all()[0]
        request = APIRequestFactory().get('/api/v1/order/')
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        
        assert response.status_code == 200


class OrderCreateTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Test for OrderView (post)
    def test_order_create_true_post (self):
        user = User.objects.all()[0]
        order_first_count = len(OrderModel.objects.all())

        data = {
            "comment": "comment",
            "pick_up_point": 1,
            "date_of_pick_up": "2024-07-10",
            "time_of_pick_up": "15.00-16.00" 
            }
        request = APIRequestFactory().post('/api/v1/order/',data)
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        order_second_count = len(OrderModel.objects.all())        
        assert (order_first_count +1 ) == (order_second_count)

    def test_order_create_without_point_post (self):
        user = User.objects.all()[0]
        order_first_count = len(OrderModel.objects.all())

        data = {
            "comment": "comment",
            "date_of_pick_up": "2024-07-10",
            "time_of_pick_up": "10.00-11.00" 
            }
        request = APIRequestFactory().post('/api/v1/order/',data)
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        order_second_count = len(OrderModel.objects.all())        
        assert (order_first_count == order_second_count)

    def test_order_create_without_date_post (self):
        user = User.objects.all()[0]
        order_first_count = len(OrderModel.objects.all())

        data = {
            "comment": "comment",
            "pick_up_point": 1,
            "time_of_pick_up": "10.00-11.00" 
            }
        request = APIRequestFactory().post('/api/v1/order/',data)
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        order_second_count = len(OrderModel.objects.all())        
        assert (order_first_count == order_second_count)

    def test_order_create_without_time_post (self):
        user = User.objects.all()[0]
        order_first_count = len(OrderModel.objects.all())

        data = {
            "comment": "comment",
            "pick_up_point": 1,
            "date_of_pick_up": "2024-07-10", 
            }
        request = APIRequestFactory().post('/api/v1/order/',data)
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        order_second_count = len(OrderModel.objects.all())        
        assert (order_first_count == order_second_count)