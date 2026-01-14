from django.urls import path
from .views import TaskListCreateAPIView


urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='taskListCreateAPIView'),
]
