from rest_framework.test import APIRequestFactory, APITestCase
from apps.users.models import User
from apps.shop.views import OrdersUserView
from rest_framework import status
from rest_framework.test import force_authenticate

# Test for OrdersUserView (get)
class OrdersViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_orders_view_get(self):
        user = User.objects.all()[0]
        request = APIRequestFactory().get('/api/v1/orders/')
        force_authenticate(request, user=user)
        response = OrdersUserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_orders_view_false_get(self):
        request = APIRequestFactory().get('/api/v1/orders/')
        force_authenticate(request)
        response = OrdersUserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)