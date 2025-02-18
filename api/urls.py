from django.urls import path
from .views import (
        EmployeesListCreate,
        EmployeesRetrieveUpdateDestroy,
        )

urlpatterns = [
    path('', EmployeesListCreate.as_view(), name='employees-list-create'),
    path('<int:pk>/', EmployeesRetrieveUpdateDestroy.as_view(), name='employees-update-destroy'),
]

