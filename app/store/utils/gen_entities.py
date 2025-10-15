import random
from itertools import count

from faker import Faker
from faker.providers import BaseProvider


class CatProdProvider(BaseProvider):
    categories = (f'Категория {num}' for num in count(1, 1))
    products = (f'Товар {num}' for num in count(1, 1))

    def category(self):
        return next(self.categories)

    def product(self):
        return next(self.products)


fkr = Faker('ru_RU')
fkr.add_provider(CatProdProvider)
