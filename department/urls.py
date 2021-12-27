"""department URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from staff.views import (
    DepartmentListAPIView,
    StaffRetrieveDestroyAPIView,
    StaffListCreateAPIView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(title="Staff Departments API", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"department", DepartmentListAPIView, basename="department")


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("staff/", StaffListCreateAPIView.as_view(), name="staff_list_create"),
    path(
        "staff/<int:pk>/",
        StaffRetrieveDestroyAPIView.as_view(),
        name="staff_retrieve_delete",
    ),
    *router.urls,
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

]
