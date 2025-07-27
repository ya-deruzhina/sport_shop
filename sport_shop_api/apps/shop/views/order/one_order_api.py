from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from apps.shop.models import OrderModel, ProductInOrder

from rest_framework.views import APIView
from rest_framework.response import Response

from core import IsActive

class OneOrdersUserView(APIView):
    permission_classes = (IsActive,)
    def get(self,request, order_id):
        try:
            order = OrderModel.objects.get(id=order_id)
                
        except:
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:        
            all_products = ProductInOrder.objects.filter(order=order_id)
            one_product_in_order = {}
            all_price = round(order.total_money,2)
            for m in range(0,(len(all_products))):
                one_product_name = all_products [m].product.name
                one_product_count = all_products[m].count
                one_product = [{"product":one_product_name, "count":one_product_count}]
                one_product_in_order[m] = one_product
                order_time = order.order_time.strftime("%H:%M:%S - %d.%m.%Y ")
                
                product = {
                    "id":order.id,
                    "order_time": order_time,
                    "comment": order.comment,
                    "name": order.name, 
                    "email": order.email,
                    "pick_up_point": order.pick_up_point.adres,
                    "date_of_pick_up": order.date_of_pick_up,
                    "time_of_pick_up": order.time_of_pick_up,
                    "all_price":all_price,
                    # "one_product_in_order":one_product_in_order,
                    }
                  
                # import pdb; pdb.set_trace()
   
            # count_product = one_product_in_order.keys()
            # template = loader.get_template("order/one_order_const.html")
            context = {
                "product":product,
                "one_product_in_order":one_product_in_order,
            }
            # return HttpResponse(template.render(context,request))
            return Response (context)