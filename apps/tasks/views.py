from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    

class TaskMarkComplete(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer