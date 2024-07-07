from rest_framework.test import APIRequestFactory, APITestCase
from apps.users.models import User
from apps.shop.views import RatingView
from rest_framework import status
from rest_framework.test import force_authenticate
from apps.shop.models import GoodsModel, RatingOfGoodsModel

from django.urls import reverse

# Test for RatingView by user+product (post)
class RatingViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_rating_view_post(self):
        user = User.objects.all()[0]
        product = GoodsModel.objects.all()[0]
        data = {"rating":5}
        request = APIRequestFactory().post('api/v1/rating/',data)
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id = product.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        rating_by_product = RatingOfGoodsModel.objects.filter(product_id = product.id).order_by('-id')[0]
    
        assert rating_by_product.rating == data['rating']
        assert rating_by_product.product == product
        assert rating_by_product.author == user

        item = response.data

        self.assertEqual(item['information']['author'], rating_by_product.author.id)
        self.assertEqual(item['information']['rating'], rating_by_product.rating)
        self.assertEqual(item['information']['product'], rating_by_product.product.id)



    def test_rating_false_rating_view_post(self):
        user = User.objects.all()[0]
        product_id = GoodsModel.objects.all()[0].id
        data = {"rating":"mistake"}
        request = APIRequestFactory().post('api/v1/rating/',data)
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id  = product_id)
        assert response.status_code == 302

    def test_rating_no_rating_view_post(self):
        user = User.objects.all()[0]
        product_id = GoodsModel.objects.all()[0].id
        request = APIRequestFactory().post('api/v1/rating/')
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id  = product_id)
        assert response.status_code == 302
        

    def test_rating_false_product_id_view_post(self):
        user = User.objects.all()[0]
        product_id = 999999999999999999999
        data = {"rating":5}
        request = APIRequestFactory().post('api/v1/comment/',data)
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id = product_id)

        assert response.status_code == 302