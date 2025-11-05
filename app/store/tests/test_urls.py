import pytest
from django.urls import reverse


def test_index_view(client):
    url = reverse('store:index')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_products_view(client):
    url = reverse('store:products')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_product_detail_view(client, products):
    url = reverse('store:product', args=(products[0].pk,))
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_product_view(client):
    url = reverse('store:add_product')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_product_view(client, products):
    url = reverse('store:edit_product', args=(products[0].pk,))
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_product_view(client, products):
    url = reverse('store:remove_product', args=(products[0].pk,))
    response = client.get(url)

    assert response.status_code == 200
