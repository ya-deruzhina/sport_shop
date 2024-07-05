from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect

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
    # Оставить Отзыв о Пицце
    def post(self,request, product_id):
        try:
            data = {"user":request.user.id, "product":product_id,"rating":(request.POST.get('rating'))}
            serializer = RatingSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except Exception as exs:
            print ('Warming!!!', exs)   
            template = loader.get_template("main/page_404.html")
            return HttpResponse(template.render())
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")