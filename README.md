# Django App

## Instruments needed
> - docker / docker compose
> - uv

## Launch instruction
```sh
docker compose up --build -d

uv sync

cd app/

python manage.py migrate

# <num_categories> и <num_products> не обязтельны
# <num_categories> по дефолту - 10
# <num_products> по дефолту - 50
python manage.py fill_db <num_categories> <num_products>

python manage.py createsuperuser <username>

python manage.py runserver
```