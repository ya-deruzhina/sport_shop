from rest_framework.test import APIRequestFactory, APITestCase
from apps.shop.views import ProductView
from rest_framework import status
from apps.shop.models import GoodsModel, CommentOfGoodsModel, RatingOfGoodsModel

from django.urls import reverse

# Test for ProductView (get)
class ProductViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_product_view_get(self):
        product = GoodsModel.objects.all()[0]
    
        request = APIRequestFactory().get('/api/v1/product/')
        response = ProductView.as_view()(request,product_id = product.id)
        item = response.data
        
        assert response.status_code == 200

        self.assertEqual(item['information']['id'], product.id)
        self.assertEqual(item['information']['name'], product.name)
        self.assertEqual(item['information']['description'], product.description)
        self.assertEqual(item['information']['price'], product.price)
        self.assertEqual(item['information']['id_parent'], product.id_parent)

        assert item['system']['comment'] != None
        assert item['system']['rating'] != None


    def test_product_false_view_get(self):
        product_id = 999999999999999999999

        request = APIRequestFactory().get('/api/v1/product/')
        response = ProductView.as_view()(request, product_id = product_id)
        assert response.status_code == 302

