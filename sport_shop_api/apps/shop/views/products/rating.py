from django.http import HttpResponseRedirect
from core import IsActive

from apps.shop.serializers import RatingSerializer
from apps.shop.models import RatingOfProductsModel

from rest_framework.views import APIView  


class RatingView(APIView):
    permission_classes = (IsActive,)
    # leave a mark (rating)
    def post(self,request, product_id):
        all_ratings = RatingOfProductsModel.objects.filter(author=request.user.id,product=product_id)

        if len(all_ratings) == 0:
            try:
                data = {"author":request.user.id, "product":product_id,"rating":(request.data['rating'])}
                serializer = RatingSerializer(data=data)
                serializer.is_valid(raise_exception=True)
        
            except:
                return HttpResponseRedirect ("/api/v1/404_error/")
            
            else:
                serializer.save()
                return HttpResponseRedirect (f"/api/v1/product/{product_id}/")
            
        else:
            rating_new = RatingOfProductsModel.objects.get(author=request.user.id,product=product_id)
            rating_new.rating = request.data['rating']
            rating_new.save()
            return HttpResponseRedirect (f"/api/v1/product/{product_id}/")