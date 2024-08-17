from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shop.models import ProductsModel
from apps.shop.serializers import CatalogSerializer

class CatalogView(APIView):  
    
    def get(self,request):
        products = ProductsModel.objects.all()
        products_with_filter = {"count":(len(products)),"next":"null","previous":"null"}
        results = []
        for product in products:
            results.append (CatalogSerializer(instance=product).data)
        products_with_filter['results'] = results
        return Response (products_with_filter)