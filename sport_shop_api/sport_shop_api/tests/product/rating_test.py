from rest_framework.test import APIRequestFactory, APITestCase
from apps.users.models import User
from apps.shop.views import RatingView
from rest_framework import status
from rest_framework.test import force_authenticate
from apps.shop.models import ProductsModel, RatingOfProductsModel

from django.urls import reverse

from sport_shop_api.tests.index import Index    

# Test for RatingView by user+product (post)
class RatingViewTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    def test_rating_view_post(self):
        user = User.objects.all()[0]
        product = ProductsModel.objects.all()[0]
        data = {"rating":5}
        request = APIRequestFactory().post('api/v1/rating/',data)
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id = product.id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        rating_by_product = RatingOfProductsModel.objects.filter(product_id = product.id).filter(author_id = user.id).order_by('-id')[0]

        assert rating_by_product.rating == data['rating']
        assert rating_by_product.product == product
        assert rating_by_product.author == user




    def test_rating_false_rating_view_post(self):
        user = User.objects.all()[0]
        product_id = ProductsModel.objects.all()[0].id
        data = {"rating":"mistake"}
        request = APIRequestFactory().post('api/v1/rating/',data)
        force_authenticate(request, user=user)
        response = RatingView.as_view()(request,product_id  = product_id)
        assert response.status_code == 302

    def test_rating_no_rating_view_post(self):
        user = User.objects.all()[0]
        product_id = ProductsModel.objects.all()[0].id
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