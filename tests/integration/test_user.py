import pytest
from django.urls import reverse
from rest_framework import status

from backend.core.models import User


@pytest.mark.django_db
def test_create_valid(api_client):
    resp = api_client.post(
        reverse("user-list"),
        {
            "email": "user@example.com",
            "password": "an-example-password",
            "first_name": "User",
            "last_name": "Example",
        },
    )

    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.data["email"] == "user@example.com"
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_retrieve_current_valid(api_client, user_factory):
    user = user_factory(name="user", permissions=[])
    api_client.force_authenticate(user=user)
    resp = api_client.get(reverse("user-logged"))

    assert resp.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_retrieve_current_invalid(api_client, user_factory):
    resp = api_client.get(reverse("user-logged"))

    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
