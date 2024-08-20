from rest_framework.test import APIRequestFactory, APITestCase
from apps.users.models import User
from apps.shop.views import CommentView
from rest_framework import status
from rest_framework.test import force_authenticate
from apps.shop.models import ProductsModel, CommentOfProductsModel

from django.urls import reverse
from internals.tests.index import Index

# Test for CommentViewы by user+product (post)
class CommentViewTestCase(APITestCase):
    Index()
    fixtures=['dump_data'] 

    def test_comment_view_post(self):
        user = User.objects.all()[0]
        product = ProductsModel.objects.all()[0]
        data = {"comment":"comment"}
        request = APIRequestFactory().post('api/v1/comment/',data)
        force_authenticate(request, user=user)
        response = CommentView.as_view()(request,product_id = product.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        comment_by_product = CommentOfProductsModel.objects.filter(product_id = product.id).order_by('-id')[0]
    
        assert comment_by_product.comment == data['comment']
        assert comment_by_product.product == product
        assert comment_by_product.author == user

        item = response.data

        self.assertEqual(item['information']['author'], comment_by_product.author.id)
        self.assertEqual(item['information']['comment'], comment_by_product.comment)
        self.assertEqual(item['information']['product'], comment_by_product.product.id)



    def test_comment_false_comment_view_post(self):
        user = User.objects.all()[0]
        product_id = ProductsModel.objects.all()[0].id
        request = APIRequestFactory().post('api/v1/comment/')
        force_authenticate(request, user=user)
        response = CommentView.as_view()(request,product_id  = product_id)
        assert response.status_code == 302
        

    def test_comment_false_product_id_view_post(self):
        user = User.objects.all()[0]
        product_id = 999999999999999999999
        data = {"comment":"comment"}
        request = APIRequestFactory().post('api/v1/comment/',data)
        force_authenticate(request, user=user)
        response = CommentView.as_view()(request,product_id = product_id)

        assert response.status_code == 302