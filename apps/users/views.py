from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class UserRegistration(CreateAPIView):
    serializer_class = UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]