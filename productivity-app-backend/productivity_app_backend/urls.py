from django.urls import path, include, include

urlpatterns = [
    path('api/', include('tasks.urls')),
    path('api/habits/', include('habits.urls')),
    path('api/auth/', include('rest_framework.urls')),
]