from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.template import loader

import json

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.shop.models import GoodsModel
from apps.shop.serializers import CatalogSerializer

class CatalogView(APIView):
    # All products from DB
    def get(self,request):
        catalog = GoodsModel.objects.all()

        # template = loader.get_template("catalog/catalog.html")
        # context = {
        #     "catalog":catalog,
        # }
        # return HttpResponse(template.render(context,request))

        working_services = [CatalogSerializer (instance=working_service).data for working_service in GoodsModel.objects.all()]
        return Response ({'Catalog':working_services})