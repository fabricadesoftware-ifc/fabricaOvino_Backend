from django.core.management.base import BaseCommand

from .data.category import category as dcategory
from backend.core.models import Category


class Command(BaseCommand):
    help = 'Populate database'

    def handle(self, *args, **options):
        for category in dcategory:
            try:
                save_category(category)
            except Exception as e:
                print(e, type(e))


def save_category(data):
    category = Category(**data)
    category.save()
