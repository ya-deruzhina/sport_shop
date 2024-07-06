from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from apps.shop.models import GoodsModel,CommentOfGoodsModel,RatingOfGoodsModel
from apps.shop.forms import CommentForm, RatingForm
from apps.shop.serializers import CatalogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Page of one product 
class ProductView(APIView):
    def get (self,request,product_id):
        try:
            product = GoodsModel.objects.filter(id=product_id)
            comment = CommentOfGoodsModel.objects.filter(product=product_id).order_by('id')
            rating = RatingOfGoodsModel.objects.filter(product=product_id)

            product = [CatalogSerializer (instance=working_service).data for working_service in product]

        except:
                return HttpResponseRedirect ("/404_error/")
        else:     
            if len(rating) > 0:
                for i in rating:
                    i += i
                rating = i/len(rating)
            else:
                rating = "No Rating"
            if len (comment) == 0:
                comment = "No Comment" 

            one_product = {'information':product, 'comment':comment, 'rating':rating}

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
        return Response ({"Product": one_product})



