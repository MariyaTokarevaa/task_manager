
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

    filterset_fields = {
        'completed': ['exact'],
        'tags': ['exact'],
        'due_date': ['exact', 'lt', 'gt'],
        'creation_date': ['exact', 'lt', 'gt'],
    }
    ordering_fields = ['due_date', 'creation_date', 'description']
    ordering = ['creation_date']
