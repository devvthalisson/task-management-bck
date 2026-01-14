from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='userListCreate'),
    path(
        'users/account/<int:pk>',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='userRetrieveUpdateDestroyAPIView',
    ),
]
