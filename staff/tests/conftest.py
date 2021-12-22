import pytest
from pytest_factoryboy import register

from staff.tests.factories import (
    DepartmentFactory,
    StaffFactory,
    UserFactory,
)

register(DepartmentFactory)
register(StaffFactory)
register(UserFactory)


@pytest.fixture
def client_authenticated(client, user):
    client.force_login(user=user)
    return client
