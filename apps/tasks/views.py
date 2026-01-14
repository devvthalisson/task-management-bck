from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer, TaskChangeStatusSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

class TaskChangeStatus(UpdateAPIView):
    serializer_class = TaskChangeStatusSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

