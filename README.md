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

python manage.py createsuperuser <username>
```