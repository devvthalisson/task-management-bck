from django.urls import path
from .views import TaskListCreateAPIView, TaskChangeStatus, TaskRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='taskListCreateAPIView'),
    path('tasks/<int:pk>/status/', TaskChangeStatus.as_view(), name='taskChangeStatus'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='taskRetrieveUpdateDestroyAPIView')
]
