from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

app_name = 'myapp'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
]
