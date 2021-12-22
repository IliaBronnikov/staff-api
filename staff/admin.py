from django.contrib import admin

from .models import Department, Staff


class StaffInline(admin.TabularInline):
    model = Staff


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [StaffInline]
    pass


class StaffAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Staff, StaffAdmin)
