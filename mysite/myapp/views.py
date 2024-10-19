from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .serializers import TaskSerializer
from django.utils import timezone
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

    def create(self, request):
        self.validate_due_date(request.data.get('due_date'))

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        task = self.get_object()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        task = self.get_object()
        serializer = self.get_serializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        task = self.get_object()
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def validate_due_date(self, due_date):
        """Check that the due date is not in the past."""
        if due_date:
            if timezone.now().date() > timezone.datetime.strptime(due_date, '%Y-%m-%d').date():
                raise ValidationError("Due date cannot be in the past.")