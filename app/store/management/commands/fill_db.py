import random

from django.core.management.base import BaseCommand

from store.models import Category, Product
from store.utils.gen_entities import fkr


class Command(BaseCommand):
    help = 'Fill Categories and Products with Random data'

    def add_arguments(self, parser):
        parser.add_argument('ncats', nargs='?', type=int, default=10)
        parser.add_argument('nprods', nargs='?', type=int, default=50)

    @staticmethod
    def add_categories(num: int):
        for cat in range(num):
            Category.objects.create(name=fkr.category())

    @staticmethod
    def get_categories_ids():
        return [cat.pk for cat in Category.objects.all()]

    def add_products(self, num: int):
        for cat in range(num):
            Product.objects.create(
                name=fkr.product(),
                category_id=random.choice(self.get_categories_ids()),
                price=random.uniform(100, 1000),
            )

    def handle(self, *args, **options):
        self.add_categories(options['ncats'])
        self.add_products(options['nprods'])
