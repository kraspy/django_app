import pytest
from bs4 import BeautifulSoup
from django.urls import reverse


@pytest.mark.django_db
def test_index_page_template(client):
    url = reverse('store:index')
    res = client.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    title = soup.find('h1')

    assert title.text.strip() == 'Welcome to Our Django Shop!'
