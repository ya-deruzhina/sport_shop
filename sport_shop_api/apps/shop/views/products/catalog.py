from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from rest_framework import pagination

from apps.shop.models import ProductsModel
from apps.shop.serializers import CatalogSerializer    

class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class CatalogListView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = CatalogSerializer
    pagination_class = DefaultPagination

    # filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    # search_fields = ['price','currency']
    # # Чтобы работал в запросе писать ordering=, чтобы в обратном
    # # порядке сортировка - поставить минус. Если надо по любому
    # # полю, то пишем '__all__'
    # ordering_fields = ['price','currency']
    # pagination_class = DefaultPagination
    # # import pdb; pdb.set_trace()    
    
    # def get_queryset(self):
    #     max_price = self.request.query_params.get('max_price')
    #     if max_price:
    #         return WalletSerial.objects.filter(price__lte=max_price)
    #     return WalletSerial.objects.all()
    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return services_serializers.WalletSerializer
    #     return services_serializers.WalletSerializer