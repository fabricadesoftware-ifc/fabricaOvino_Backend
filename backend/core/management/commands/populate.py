from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from .data.data_populate import (
    breeds, categorys, feeds, lots, users)
from backend.core.models import (
    Breed, Category, Feed, Lots, User)


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        save_breed(breeds)
        save_category(categorys)
        save_feed(feeds)
        save_lot(lots)
        save_user(users)


def save_breed(data):
    for b in data:
        try:
            breed = Breed(**b)
            breed.save()
        except Exception as e:
            print("BREED: ", e, type(e))


def save_category(data):
    for c in data:
        try:
            category = Category(**c)
            category.save()
        except Exception as e:
            print("CATEGORY: ", e, type(e))


def save_feed(data):
    for f in data:
        try:
            feed = Feed(**f)
            feed.save()
        except Exception as e:
            print("FEED: ", e, type(e))


def save_lot(data):
    for l in data:
        try:
            lot = Lots(**l)
            lot.save()
        except Exception as e:
            print("LOTS: ", e, type(e))


def save_user(data):
    for u in data:
        try:
            user = User(**u)
            user.password = make_password(user.password)
            user.save()
        except Exception as e:
            print("USER: ", e, type(e))
