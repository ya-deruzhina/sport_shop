from rest_framework.generics import RetrieveAPIView
from core.loggers import IsActive
from ..serializers import UserSerializer


class CurrentUserView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsActive,)

    def get_object(self):
        return self.request.user
