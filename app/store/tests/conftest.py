from random import randint

import pytest

from store.models import Product


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
