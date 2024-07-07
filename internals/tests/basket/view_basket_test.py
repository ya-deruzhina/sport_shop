from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, BasketModel, CatalogModel
from pizza_lisa.views import BasketView,BasketDelete, BasketAdd
from rest_framework import status
from rest_framework.test import force_authenticate

from django.urls import reverse


# Тест на BasketView (get)
class BasketViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_only_view_basket_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/basket/')
        force_authenticate(request, user=user)
        response = BasketView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_view_basket_without_token_get(self):
        response = self.client.get(
            reverse('view-basket')
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
