from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from .data.data_populate import (
    breeds, categorys, feeds, lots, preg_diagonis, users, sheeps)
from backend.core.models import (
    Breed, Category, Feed, Lots, PregnancyDiagnosis, User, Sheep)


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        save_breed(breeds)
        save_category(categorys)
        save_feed(feeds)
        save_lot(lots)
        save_user(users)
        save_sheep(sheeps)
        save_pregnance_diagnosis(preg_diagonis)


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


def save_pregnance_diagnosis(data):
    for p in data:
        try:
            sheep_instance = Sheep.objects.get(pk=p["sheep"])
            user_instance = User.objects.get(pk=p["user"])

            p["sheep"] = sheep_instance
            p["user"] = user_instance

            preg_diagonise = PregnancyDiagnosis(**p)
            preg_diagonise.save()
        except Exception as e:
            print("PREGNANCY_DIAGNOSIS: ", e, type(e))


def save_user(data):
    for u in data:
        try:
            user = User(**u)
            user.password = make_password(user.password)
            user.save()
        except Exception as e:
            print("USER: ", e, type(e))


def save_sheep(data):
    for s in data:
        try:
            breed_instance = Breed.objects.get(pk=s["breed"])
            category_instance = Category.objects.get(pk=s["category"])
            lots_instance = Lots.objects.get(pk=s["lots"])

            s["breed"] = breed_instance
            s["category"] = category_instance
            s["lots"] = lots_instance

            sheep = Sheep(**s)
            sheep.save()
        except Exception as e:
            print("SHEEP: ", e, type(e))
