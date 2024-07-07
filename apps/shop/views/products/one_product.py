from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from apps.shop.models import GoodsModel,CommentOfGoodsModel,RatingOfGoodsModel
from apps.shop.forms import CommentForm, RatingForm
from apps.shop.serializers import CatalogSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Page of one product 
class ProductView(APIView):
    def get (self,request,product_id):
        try:
            product = GoodsModel.objects.get(id=product_id)
            comment = CommentOfGoodsModel.objects.filter(product=product_id).order_by('id')
            rating = RatingOfGoodsModel.objects.filter(product=product_id)
            
            serializer = CatalogSerializer(instance=product).data

        except:
                return HttpResponseRedirect ("/api/v1/404_error/")
        else:     
            if len(rating) > 0:
                for i in rating:
                    i += i
                rating = i/len(rating)
            else:
                rating = "No Rating"
            if len (comment) == 0:
                comment = "No Comment" 

            one_product = {'information':serializer, "system":{'comment':comment, 'rating':rating}}

        # template = loader.get_template("catalog/product.html")
        # context = {
                # "product" : one_product,
            # }

        # return HttpResponse(template.render(context,request))
        return Response (one_product)



