from apps.shop.models import ProductsModel
from apps.shop.serializers import CatalogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class FilterAmountOverView(APIView):
    # 
    def get(self,request, query):
        products = ProductsModel.objects.filter(amount__gte = query)
        products_with_filter = {"count":(len(products)),"next":"null","previous":"null"}
        results = []
        for product in products:
            results.append (CatalogSerializer(instance=product).data)
        products_with_filter['results'] = results
        return Response (products_with_filter)