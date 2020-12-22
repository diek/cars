import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Car_list_view():
    instance1 = test_helpers.create_car_Car()
    instance2 = test_helpers.create_car_Car()
    client = Client()
    url = reverse("car_Car_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Car_create_view():
    client = Client()
    url = reverse("car_Car_create")
    data = {
        "year": 1,
        "model": "text",
        "base_color": "text",
        "size": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Car_detail_view():
    client = Client()
    instance = test_helpers.create_car_Car()
    url = reverse("car_Car_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Car_update_view():
    client = Client()
    instance = test_helpers.create_car_Car()
    url = reverse("car_Car_update", args=[instance.pk, ])
    data = {
        "year": 1,
        "model": "text",
        "base_color": "text",
        "size": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Make_list_view():
    instance1 = test_helpers.create_car_Make()
    instance2 = test_helpers.create_car_Make()
    client = Client()
    url = reverse("car_Make_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Make_create_view():
    client = Client()
    url = reverse("car_Make_create")
    data = {
        "make": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Make_detail_view():
    client = Client()
    instance = test_helpers.create_car_Make()
    url = reverse("car_Make_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Make_update_view():
    client = Client()
    instance = test_helpers.create_car_Make()
    url = reverse("car_Make_update", args=[instance.pk, ])
    data = {
        "make": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
