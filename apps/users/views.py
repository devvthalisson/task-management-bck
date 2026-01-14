from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer
from .models import User


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer