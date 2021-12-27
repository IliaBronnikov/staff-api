from django.contrib import admin

from .models import Department, Staff, Project


class StaffInline(admin.TabularInline):
    model = Staff

class ProjectInline(admin.TabularInline):
    model = Project


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [StaffInline, ProjectInline]
    pass


class StaffAdmin(admin.ModelAdmin):

    # fields = ('full_name', 'photo', 'position', 'salary', 'age', 'department', 'project')
    pass


class ProjectAdmin(admin.ModelAdmin):
    # inlines = [StaffInline]
    pass


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Project, ProjectAdmin)

