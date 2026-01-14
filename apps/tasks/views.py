from rest_framework.generics import ListCreateAPIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)