from celery import shared_task

@shared_task
def add_product(product_name):
    print(f'New product added: {product_name}')
    return f'New product added: {product_name}'