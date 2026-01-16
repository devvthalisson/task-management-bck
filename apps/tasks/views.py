from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer, TaskChangeStatusSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .filters import TaskFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from .paginations import TaskResultsSetPagination


class TaskListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-updated_at')

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

