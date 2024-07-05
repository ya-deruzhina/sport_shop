from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from apps.shop.models import GoodsModel,CommentOfGoodsModel,RatingOfGoodsModel
from apps.shop.forms import CommentForm, RatingForm

from rest_framework.views import APIView

# Page of one product 
class ProductView(APIView):
    def get (self,request,product_id):
        try:
            product = GoodsModel.objects.get(id=product_id)
            comment = CommentOfGoodsModel.objects.filter(product=product_id).order_by('id')
            rating = RatingOfGoodsModel.objects.filter(product=product_id)

            for i in rating:
                 i += i
            rating = i/len(rating)

        except:
                return HttpResponseRedirect ("/404_error/")
        else:     
            # template = loader.get_template("catalog/pizza.html")
        # context = {
                # "product" : product,
                # "form_comment":CommentForm(),
                # "form_rating":RatingForm(),
                # "comment":comment,
                # "price":price,
                # "discont":discont,
            # }

        # return HttpResponse(template.render(context,request))
            return HttpResponseRedirect ("")



