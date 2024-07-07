from django.http import HttpResponseRedirect
from core import IsActive

from apps.shop.serializers import RatingSerializer

from rest_framework.views import APIView
from rest_framework.response import Response      


class RatingView(APIView):
    permission_classes = (IsActive,)
    # leave a mark (rating)
    def post(self,request, product_id):
        try:
            data = {"author":request.user.id, "product":product_id,"rating":(request.data['rating'])}
            serializer = RatingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except:
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            serializer.save()
            # return HttpResponseRedirect ("")
            return Response ({"information":serializer.data})
        