from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.users.urls')),
    path('content/', include('apps.tasks.urls')),
]
