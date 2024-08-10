from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class Page404(GenericAPIView):
    # 404 Page
    def get(self,request):
        status = HTTP_400_BAD_REQUEST
            # template = loader.get_template("order/order.html")
            # context = {
            # }
            # return HttpResponse(template.render(context,request))
        return Response({'errors': '404'}, status=status)
        return JsonResponse ({"Page":404})
