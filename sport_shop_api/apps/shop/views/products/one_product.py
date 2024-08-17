from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

from apps.shop.models import ProductsModel,CommentOfProductsModel,RatingOfProductsModel
from apps.shop.serializers import CatalogSerializer, CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Page of one product 
class ProductView(APIView):
    def get (self,request,product_id):
        try:
            # import pdb; pdb.set_trace()
            product = ProductsModel.objects.get(id=product_id)
            comment_filter = CommentOfProductsModel.objects.filter(product=product_id).order_by('id')
            rating_filter = RatingOfProductsModel.objects.filter(product=product_id)

            serializer = CatalogSerializer(instance=product).data

        except:
                return HttpResponseRedirect ("/api/v1/404_error/")
        else:
            rating_all = 0
            comment = [{}]     
            
            if len(rating_filter) > 0:
                for i in rating_filter:
                    rating_all += i.rating
                rating = rating_all/len(rating_filter)
            else:
                rating = "No Rating"
            if len (comment_filter) == 0:
                comment = "No Comment"
            else:
                for n in range (len (comment_filter)):
                    serializer_comment = CommentSerializer(instance=comment_filter[n]).data
                    comment[0][comment_filter[n].author.id] = [serializer_comment]

            one_product = {'information':serializer, "system":{'comment':comment, 'rating':rating}}

        # template = loader.get_template("catalog/product.html")
        # context = {
                # "product" : one_product,
            # }

        # return HttpResponse(template.render(context,request))
        return Response (one_product)



