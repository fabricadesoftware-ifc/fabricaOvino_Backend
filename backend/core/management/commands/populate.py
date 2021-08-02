from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from .data.data_populate import (
    births, birth_sheeps, breeds, categorys, feeds, lots, preg_diagonis, users, shearings, sheeps)
from backend.core.models import (
    Birth, Breed, Category, Feed, Lots, PregnancyDiagnosis, User, Shearing, Sheep)


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        save_breed(breeds)
        save_category(categorys)
        save_feed(feeds)
        save_lot(lots)
        save_user(users)
        save_sheep(sheeps)
        save_pregnancy_diagnosis(preg_diagonis)
        save_shearing(shearings)
        save_birth(births, birth_sheeps)


def save_birth(data, data_sheeps):
    for b in data:
        try:
            sheep_instance = Sheep.objects.get(pk=b["sheep"])
            user_instance = User.objects.get(pk=b["user"])

            b["sheep"] = sheep_instance
            b["user"] = user_instance

            birth = Birth(**b)
            birth.save()

            save_sheep(data_sheeps)
        except Exception as e:
            print("BIRTH: ", e, type(e))


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
    for ld in data:
        try:
            lot = Lots(**ld)
            lot.save()
        except Exception as e:
            print("LOTS: ", e, type(e))


def save_pregnancy_diagnosis(data):
    for p in data:
        try:
            sheep_instance = Sheep.objects.get(pk=p["sheep"])
            user_instance = User.objects.get(pk=p["user"])

            p["sheep"] = sheep_instance
            p["user"] = user_instance

            preg_diagnose = PregnancyDiagnosis(**p)
            preg_diagnose.save()
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


def save_shearing(data):
    for s in data:
        try:
            sheep_instance = Sheep.objects.get(pk=s["sheep"])
            user_instance = User.objects.get(pk=s["user"])

            s["sheep"] = sheep_instance
            s["user"] = user_instance

            shearing = Shearing(**s)
            shearing.save()
        except Exception as e:
            print("SHEARING: ", e, type(e))


def save_sheep(data):
    for s in data:
        try:
            if s["birth"] is not None:
                birth_instance = Birth.objects.get(pk=s["birth"])
                s["birth"] = birth_instance

            if s["lots"] is not None:
                lots_instance = Lots.objects.get(pk=s["lots"])
                s["lots"] = lots_instance

            breed_instance = Breed.objects.get(pk=s["breed"])
            category_instance = Category.objects.get(pk=s["category"])

            s["breed"] = breed_instance
            s["category"] = category_instance

            sheep = Sheep(**s)
            sheep.save()
        except Exception as e:
            print("SHEEP: ", e, type(e))
