from django.http import HttpResponseRedirect

from apps.shop.serializers import CommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication     



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return   # To not perform the csrf check previously happening
    
class Comment(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # Leave a comment
    def post(self,request, product_id):
        try:
            data = {"author":request.user.id, "product":product_id,"comment":(request.POST.get('comment'))}
            serializer = CommentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except: 
            return HttpResponseRedirect ("/404_error/")
        
        else:
            serializer.save()
            return HttpResponseRedirect ("")