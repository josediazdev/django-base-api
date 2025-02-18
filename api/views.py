from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeesSerializer

# Create your views here.
class EmployeesListCreate(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

    def delete(self, request, *args, **kwargs):
        Employees.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    lookup_field = "pk"
