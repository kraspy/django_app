import pytest

from store.forms import AddProductForm
from store.models import Product


@pytest.mark.django_db
def test_add_product_form(category_1):
    form_data = {
        'name': 'Product',
        'slug': 'product',
        'price': 100,
        'status': Product.Status.ACTIVE,
        'category': category_1.id,
    }

    form = AddProductForm(form_data)

    assert form.is_valid()
    assert form.cleaned_data['name'] == 'Product'


@pytest.mark.django_db
def test_add_product_invalid_form_without_category():
    form_data = {
        'name': 'Product',
        'slug': 'product',
        'price': 100,
        'status': Product.Status.ACTIVE,
    }

    form = AddProductForm(form_data)

    assert not form.is_valid()
