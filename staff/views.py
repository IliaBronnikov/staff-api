from django.db.models import Count, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from staff.models import Staff, Department, Project
from staff.serializers import StaffSerializer, DepartmentSerializer, DepartmentListSerializer, ProjectSerializer


class StaffPagination(LimitOffsetPagination):
    default_limit = 10


class StaffListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["full_name", "department"]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    pagination_class = StaffPagination


class StaffRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class DepartmentListAPIView(viewsets.ReadOnlyModelViewSet):
    def get_serializer_class(self):
        if self.action == "list":
            return DepartmentListSerializer
        return DepartmentSerializer

    def get_queryset(self):
        if self.action == "list":
            return Department.objects.all().annotate(
                staff_count=Count("staff"),
                total_salary=Sum("staff__salary"),
            )
        return Department.objects.all()


