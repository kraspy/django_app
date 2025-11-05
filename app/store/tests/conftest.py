from random import randint

import pytest

from store.models import Category, Product


@pytest.fixture
def products():
    return [
        Product.objects.create(
            name=f'Product{i}',
            slug=f'p-{i}',
            description=f'Description for product # {i}',
            price=randint(1, 10000),
        )
        for i in range(10)
    ]


@pytest.fixture
def category_1():
    return Category.objects.create(
        name='Category1',
        slug='cat-1',
        description='description for category 1',
    )
