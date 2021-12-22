import pytest
from django.urls import reverse

from staff.models import Staff


@pytest.mark.django_db()
def test_staff_list_api(client_authenticated, staff_factory):
    staff_url = reverse("staff_list_create")
    staff1 = staff_factory()
    staff2 = staff_factory()

    response = client_authenticated.get(staff_url)
    content = response.json()

    assert response.status_code == 200
    assert len(content["results"]) == 2
    assert content["results"][0] == {
        "pk": staff1.pk,
        "full_name": staff1.full_name,
        "position": staff1.position,
        "salary": staff1.salary,
        "age": staff1.age,
        "department": staff1.department.pk,
    }


@pytest.mark.django_db()
def test_department_list_api(client_authenticated, department_factory, staff_factory):
    department_url = reverse("department_list")
    department = department_factory()
    staffs = staff_factory.create_batch(10, department=department)
    staff_salary = sum(staff.salary for staff in staffs)

    response = client_authenticated.get(department_url)

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {
        "pk": department.pk,
        "title": department.title,
        "staff_count": len(staffs),
        "total_salary": staff_salary,
    }


@pytest.mark.django_db()
def test_staff_delete_api(client_authenticated, staff_factory):
    pk_to_remove = 2
    staff_count = 10
    staff_retrieve_delete_url = reverse(
        "staff_retrieve_delete", kwargs={"pk": pk_to_remove}
    )
    staff_factory.create_batch(staff_count)

    response = client_authenticated.delete(staff_retrieve_delete_url)

    assert response.status_code == 204
    assert not Staff.objects.filter(pk=pk_to_remove).exists()
    assert Staff.objects.count() == staff_count - 1


@pytest.mark.django_db()
def test_auth_staff_list_api(client):
    staff_url = reverse("staff_list_create")

    response = client.get(staff_url)

    assert response.status_code == 403
