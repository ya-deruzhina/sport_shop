from apps.shop.views.order.order_service import OrderServiseView

from rest_framework.views import APIView
from rest_framework.response import Response

from core import IsActive

class OneOrdersUserView(APIView):
    permission_classes = (IsActive,)
    def get(self,request, order_id):
        product = OrderServiseView.one_order(order_id)

        return Response (product)