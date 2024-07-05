from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from apps.shop.models import OrderModel, ProductInOrder

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class OrdersUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    # Connect models OrderModel and ProductInOrder by order's number
    def get(self,request):        
        orders_with_product = OrderModel.objects.filter(user=request.user.id).order_by('-order_time')
        product_in_order = {}

        for n in range (0,(len(orders_with_product))) :
            product_in_order[orders_with_product[n].id] = ProductInOrder.objects.filter(order=orders_with_product[n].id)

        numbers_orders = product_in_order.keys()

        order = {}
        for i in numbers_orders:
            try:
                orders = OrderModel.objects.get (id = i)
                all_price = orders_with_product.get(id=i).total_money            
                    
            except:
                return HttpResponseRedirect ("/404_error/")
            
            else:
        #         order_time = orders.order_time.strftime("%H:%M:%S - %d.%m.%Y ")
        #         product = {
        #             "status": orders.status,
        #             "order_time": order_time,
        #             "all_price":all_price,
        #             }      
        #         order [i] = (product)

        # template = loader.get_template("order/history_orders.html")
        # context = {
        #     "order":order,
        #     "numbers_orders":numbers_orders,
        # }
        # return HttpResponse(template.render(context,request))
                return HttpResponseRedirect ("")