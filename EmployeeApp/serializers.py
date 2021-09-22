from rest_framework import serializers
from EmployeeApp.models import Departements, Employees


class DepartmenetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departements
        fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department',
                  'DateOfJoining', 'PhotoFileName')
