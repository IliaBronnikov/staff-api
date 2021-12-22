import factory
from factory.fuzzy import FuzzyInteger, FuzzyText
from django.contrib.auth.models import User
from staff.models import (
    Staff,
    Department,
)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = FuzzyText()
    password = FuzzyText()


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    title = FuzzyText()


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    full_name = FuzzyText()
    photo = "default.jpg"
    position = FuzzyText()
    salary = FuzzyInteger(low=1)
    age = FuzzyInteger(low=1)
    department = factory.SubFactory(DepartmentFactory)
