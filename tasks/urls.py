from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StatusChoicesView, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('status-choices/', StatusChoicesView.as_view(), name='status-choices'),
]
