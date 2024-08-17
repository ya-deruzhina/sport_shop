from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.db import transaction
from django.core.mail import send_mail

from apps.users.models import User
from apps.shop.models import ProductsModel,BasketModel,OrderModel, ProductInOrder,PickUpModel
from apps.shop.serializers import OrderSerializer,OrderProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from core import IsActive


class OrderView(APIView):
    permission_classes = (IsActive,)


    # Order's page after ordering
    def get(self,request):
        try: 
            order_number = OrderModel.objects.filter(user=request.user.id).order_by('-order_time')[0].id
            order_inf = OrderSerializer(instance=OrderModel.objects.get(id=order_number)).data
            product_in_order = []
            products = ProductInOrder.objects.filter(order=order_number)
            for order in range (0,len(products)):
                # product_in_order[products[order].id] = OrderProductSerializer(instance=products[order]).data
                product_in_order.append(OrderProductSerializer(instance=products[order]).data)

        except:
            return HttpResponseRedirect ("/api/v1/404_error/")

        else:
            # template = loader.get_template("order/order.html")
            context = {
                "Your order Send": (f'Order Number {order_number}'),
                "order_inf":order_inf,
                "product":product_in_order
            }

            # return HttpResponse(template.render(context,request))
            return Response (context)


    # Forming an Order
    def post(self,request):

        with transaction.atomic():
           # Forming an Order and recording to DB Orders and Ppoducts in order
            id_user = request.user.id
            basket = BasketModel.objects.filter(user=id_user)
            if len(basket) == 0:
                return HttpResponseRedirect ("/api/v1/404_error/")
            catalog = ProductsModel.objects.all()
            price_all = 0
            n=1
            data_product = {}

            for product in basket:
                price_one = catalog.get(id = product.product_id).price
                price_one = round(price_one,2)
                price_all += price_one * product.count
                price_all = round(price_all,2)
                data_product[n] = {'count':product.count, 'product':product.product_id,'price_one':price_one}           
                n+=1

            # ! Getting client's information            
            try:
                user = request.user.username
                email = request.user.email
                comment = request.POST.get('comment')
                pick_up_point =  request.POST.get('pick_up_point')
                date_of_pick_up =  request.POST.get('date_of_pick_up')
                time_of_pick_up = request.POST.get('time_of_pick_up')
                # import pdb; pdb.set_trace()
                if len(OrderModel.objects.filter(pick_up_point = pick_up_point,date_of_pick_up=date_of_pick_up,time_of_pick_up=time_of_pick_up)) <= 4:
                    data_client = {
                        "user":id_user, 
                        "name":user,
                        "email":email,
                        "comment":comment,
                        "pick_up_point":pick_up_point,
                        "date_of_pick_up":date_of_pick_up,
                        "time_of_pick_up":time_of_pick_up,
                        "total_money":price_all
                        }
                    serializer = OrderSerializer(data=data_client)
                    serializer.is_valid(raise_exception=True)
                else:
                    return HttpResponseRedirect ("/api/v1/404_error/")
            except:              
                return HttpResponseRedirect ("/api/v1/404_error/")
            
            else:
                serializer.save()


            # Recording Product to ProductInOrder
                order_number = OrderModel.objects.filter(user=id_user).order_by('-order_time')[0].id
                for a in data_product.keys():
                    data = data_product[a]
                    price_one = round(float(data['price_one']),2)
                    data = {'order':order_number,'count':data['count'], 'product':data['product'],'price_one':price_one}
                    try:
                        serializer = OrderProductSerializer(data=data)
                        serializer.is_valid(raise_exception=True)
                    
                    except:
                        return HttpResponseRedirect ("/api/v1/404_error/")

                    else:        
                        serializer.save()

             # Deleting basket
            basket.delete()
            # Sent message
            send_mail(
                f'Order {order_number}',
                'Thank you for your order',
                'moya_powta@list.ru',
                ["moya_powta@list.ru"],
            )                
        return HttpResponseRedirect ("/api/v1/order/")