from django.http import HttpResponse, JsonResponse
from django.template import loader

from rest_framework.views import APIView

from apps.users.models import GoodsModel

class CatalogView(APIView):
    # Выводит все товары из БД
    def get(self,request):
        catalog = GoodsModel.objects.all()
        # template = loader.get_template("catalog/catalog.html")
        # context = {
            # "catalog":catalog,
            # "catalog_discont":catalog_discont,
        # }
        # return HttpResponse(template.render(context,request))
        return JsonResponse (catalog)