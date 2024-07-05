from django.http import HttpResponseRedirect

from apps.shop.serializers import RatingSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication     



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening
    
class Rating(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # leave a mark (rating)
    def post(self,request, product_id):
        try:
            data = {"user":request.user.id, "product":product_id,"rating":(int(request.POST.get('rating')))}
            serializer = RatingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except:
            return HttpResponseRedirect ("/404_error/")
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")