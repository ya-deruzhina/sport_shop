from apps.shop.models import OrderModel
from apps.shop.serializers import OrderSerializer

from core import IsActive

from rest_framework import generics
from rest_framework import pagination

class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class OrdersUserView(generics.ListAPIView):
    permission_classes = (IsActive,)
    serializer_class = OrderSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user.id).order_by('-order_time')