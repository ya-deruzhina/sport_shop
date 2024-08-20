from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from rest_framework import pagination

from apps.shop.models import ProductsModel
from apps.shop.serializers import CatalogSerializer, GoodsSearchSerializer    

class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class CatalogListView(generics.ListAPIView):
    serializer_class = GoodsSearchSerializer
    pagination_class = DefaultPagination
    ordering_fields = ['price','amount']
    
    def get_queryset(self,**kwargs):
        params = self.request.query_params

        if 'max_price' in params:
            return ProductsModel.objects.filter(price__lte=params.get('max_price'))
        
        if 'min_price' in params:
            return ProductsModel.objects.filter(price__gte=params.get('min_price'))
        
        if 'max_amount' in params:
            return ProductsModel.objects.filter(amount__lte=params.get('max_amount'))
        
        if 'min_amount' in params:
            return ProductsModel.objects.filter(amount__gte=params.get('min_amount'))
        
        if 'price_from_min' in params:
            return ProductsModel.objects.all().order_by('price')

        if 'price_from_max' in params:
            return ProductsModel.objects.all().order_by('-price')

        if 'amount_from_min' in params:
            return ProductsModel.objects.all().order_by('amount')

        if 'amount_from_max' in params:
            return ProductsModel.objects.all().order_by('-amount')
        
        return ProductsModel.objects.all()
