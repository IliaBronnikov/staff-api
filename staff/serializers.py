from rest_framework import serializers

from staff.models import Staff, Department


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("pk", "full_name", "position", "salary", "age", "department")


class DepartmentSerializer(serializers.ModelSerializer):
    staff_count = serializers.IntegerField()
    total_salary = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ("pk", "title", "staff_count", "total_salary")
