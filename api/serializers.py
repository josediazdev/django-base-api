from rest_framework import serializers
from .models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ["id", "id_card", "name", "entry_date"]
