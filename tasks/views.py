from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import STATUS_CHOICES
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

class StatusChoicesView(APIView):
    """
    View to retrieve the choices for the 'status' field.

    Returns a JSON response with the available choices.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve status choices.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: JSON response containing status choices.
        """
        return Response({"choices": [{"value": choice[0], "display_name": choice[1]} for choice in STATUS_CHOICES]}, status=status.HTTP_200_OK)


class TaskPagination(PageNumberPagination):
    """
    Pagination class for the TaskViewSet.

    Defines the page size and other pagination parameters.
    """

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on tasks.

    Allows users to create, view, update, and delete tasks.
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        """
        Retrieve tasks belonging to the authenticated user.
        Superadmins can view all tasks.

        Returns:
        - QuerySet: Filtered tasks based on the authenticated user or all tasks for superadmins.
        """
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Set the owner of the task to the authenticated user during creation.

        Parameters:
        - serializer: The serializer instance handling task creation.
        """
        serializer.save(owner=self.request.user)
