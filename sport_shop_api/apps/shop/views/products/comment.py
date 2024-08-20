from django.http import HttpResponseRedirect
from core import IsActive

from apps.shop.serializers import CommentSerializer

from rest_framework.views import APIView
  

class CommentView(APIView):
    permission_classes = (IsActive,)
    # Leave a comment
    def post(self,request, product_id):
        try:
            data = {"author":request.user.id, "product":product_id,"comment":(request.data['comment'])}
            serializer = CommentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
       
        except: 
            return HttpResponseRedirect ("/api/v1/404_error/")
        
        else:
            serializer.save()
            return HttpResponseRedirect (f"/api/v1/product/{product_id}/")