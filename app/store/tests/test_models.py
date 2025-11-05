import pytest

from store.models import Category, Product


@pytest.mark.django_db
def test_fixture_created(products, category_1):
    assert Product.objects.count() == 10
    assert Category.objects.count() == 1


@pytest.mark.django_db
def test_product_fields(products):
    assert products[0].name == 'Product0'
    assert products[0].slug == 'p-0'
    assert products[0].description == 'Description for product # 0'


@pytest.mark.django_db
def test_category_fields(category_1):
    assert category_1.name == 'Category1'
    assert category_1.slug == 'cat-1'
    assert category_1.description == 'description for category 1'
