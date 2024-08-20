from rest_framework.test import APIRequestFactory, APITestCase
from apps.shop.views import ProductView
from rest_framework import status
from apps.shop.models import ProductsModel
from apps.users.models import User

from django.urls import reverse

from unittest import mock
import pytest

from sport_shop_api.tests.index import Index

# Test for ProductView (get)
class ProductViewTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    def test_product_view_get(self):
        product = ProductsModel.objects.all()[0]
        product_id = product.id
    
        request = APIRequestFactory().get('/api/v1/product/')
        response = ProductView.as_view()(request,product_id = product_id)
        item = response.data
        assert response.status_code == 200

        self.assertEqual(item['information']['id'], product_id)
        self.assertEqual(item['information']['name'], product.name)
        self.assertEqual(item['information']['description'], product.description)
        self.assertEqual(float(item['information']['price']), float(product.price))
        

        assert item['system']['comment'] != None
        assert item['system']['rating'] != None


    def test_product_false_view_get(self):
        product_id = 999999999999999999999

        request = APIRequestFactory().get('/api/v1/product/')
        response = ProductView.as_view()(request, product_id = product_id)
        assert response.status_code == 302

