from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shop.models import GoodsModel
from apps.shop.serializers import CatalogSerializer




# class CatalogView(APIView):  
    
#     def get(self,request):
#         all_goods = GoodsModel.objects.filter(amount__gte=0)
        
#         goods = {}
#         for n in all_goods:
#             serializer_goods = CatalogSerializer(instance=n).data
#             goods[n.id] = [serializer_goods]


# #         # template = loader.get_template("catalog/catalog.html")
# #         # context = {
# #         #     "catalog":catalog,
# #         # }
# #         # return HttpResponse(template.render(context,request))
            
#         return Response ({"catalog":goods})

from rest_framework import viewsets
class CatalogViewSets(viewsets.ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = GoodsModel.objects.all()