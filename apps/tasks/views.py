from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer, TaskChangeStatusSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .filters import TaskFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from .paginations import TaskResultsSetPagination


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all().order_by('-updated_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    pagination_class = TaskResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class TaskChangeStatus(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskChangeStatusSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
    

class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

