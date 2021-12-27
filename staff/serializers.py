from rest_framework import serializers

from staff.models import Staff, Department, Project


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("pk", "full_name", "position", "salary", "age", "department")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("pk", "title", "owner")

class DepartmentListSerializer(serializers.ModelSerializer):
    staff_count = serializers.IntegerField()
    total_salary = serializers.IntegerField()

    class Meta:
        model = Department
        fields = ("pk", "title", "staff_count", "total_salary")

class DepartmentSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Department
        fields = ("pk", "title", "projects")
