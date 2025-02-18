from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework_api_key.permissions import HasAPIKey

# Create your views here.
class EmployeesListCreate(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [HasAPIKey]

    def delete(self, request, *args, **kwargs):
        Employees.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    lookup_field = "pk"
    permission_classes = [HasAPIKey]
