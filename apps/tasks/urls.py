from django.urls import path
from .views import TaskListCreateAPIView, TaskMarkComplete


urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='taskListCreateAPIView'),
    path('tasks/<int:pk>/completed/', TaskMarkComplete.as_view(), name='taskMarkComplete'),
]
