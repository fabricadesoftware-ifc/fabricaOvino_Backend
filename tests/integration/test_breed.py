import pytest
from django.urls import reverse
from rest_framework import status

from backend.core.models import Breed


@pytest.mark.django_db
def test_create_valid(api_client, user_factory):
    user = user_factory(name="user", permissions=["core.add_breed"])
    api_client.force_authenticate(user=user)

    breed_data = {"name": "Breed 1"}
    resp = api_client.post(reverse("breed-list"), breed_data)

    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], int)
    assert Breed.objects.get(pk=resp.data["id"]).name == breed_data["name"]


@pytest.mark.django_db
def test_create_unauthorized(api_client, user_factory):
    user = user_factory(name="user", permissions=[])
    api_client.force_authenticate(user=user)

    breed_data = {"name": "Breed 1"}
    resp = api_client.post(reverse("breed-list"), breed_data)

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert Breed.objects.exists() is False


@pytest.mark.django_db
def test_update_valid(api_client, user_factory):
    user = user_factory(name="user", permissions=["core.change_breed"])
    api_client.force_authenticate(user=user)

    breed = Breed.objects.create(name="Breed 1")
    resp = api_client.put(reverse("breed-detail", args=[breed.id]), {"name": "{} modified!".format(breed.name)},)

    assert resp.status_code == status.HTTP_200_OK
    assert resp.data["name"] == "{} modified!".format(breed.name)
    assert Breed.objects.get(pk=breed.id).name == "{} modified!".format(breed.name)


@pytest.mark.django_db
def test_update_unauthorized(api_client, user_factory):
    user = user_factory(name="user", permissions=[])
    api_client.force_authenticate(user=user)

    breed = Breed.objects.create(name="Breed 1")
    resp = api_client.put(reverse("breed-detail", args=[breed.id]), {"name": "{} modified!".format(breed.name)},)

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert Breed.objects.get(pk=breed.id).name == breed.name


@pytest.mark.django_db
def test_delete_valid(api_client, user_factory):
    user = user_factory(name="user", permissions=["core.delete_breed"])
    api_client.force_authenticate(user=user)

    breed = Breed.objects.create(name="Breed 1")
    resp = api_client.delete(reverse("breed-detail", args=[breed.id]),)

    assert resp.status_code == status.HTTP_204_NO_CONTENT
    assert Breed.objects.filter(pk=breed.id).exists() is False


@pytest.mark.django_db
def test_delete_unauthorized(api_client, user_factory):
    # DADO um usuário autenticado.
    user = user_factory(name="user", permissions=[])
    api_client.force_authenticate(user=user)

    breed = Breed.objects.create(name="Breed 1")
    resp = api_client.delete(reverse("breed-detail", args=[breed.id]),)

    assert resp.status_code == status.HTTP_403_FORBIDDEN
    assert Breed.objects.get(pk=breed.id).name == breed.name
