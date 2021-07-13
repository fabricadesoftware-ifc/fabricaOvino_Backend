from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from .data.data_populate import (
    breeds, categorys, feeds, users)
from backend.core.models import (
    Breed, Category, Feed, User)


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        save_breed(breeds)
        save_category(categorys)
        save_feed(feeds)
        save_user(users)


def save_breed(data):
    for b in data:
        try:
            breed = Breed(**b)
            breed.save()
        except Exception as e:
            print(e, type(e))


def save_category(data):
    for c in data:
        try:
            category = Category(**c)
            category.save()
        except Exception as e:
            print(e, type(e))


def save_feed(data):
    for f in data:
        try:
            feed = Feed(**f)
            feed.save()
        except Exception as e:
            print(e, type(e))


def save_user(data):
    for u in data:
        try:
            user = User(**u)
            user.password = make_password(user.password)
            user.save()
        except Exception as e:
            print(e, type(e))
