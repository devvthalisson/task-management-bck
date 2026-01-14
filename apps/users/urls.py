from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserRegistration
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(), name='userRegistration'),

    path('users/', UserListCreateAPIView.as_view(), name='userListCreate'),
    path(
        'users/account/<int:pk>',
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name='userRetrieveUpdateDestroyAPIView',
    ),
]
