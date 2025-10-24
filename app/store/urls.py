from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.page_index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product, name='product'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit_product'),
    path(
        'products/delete/<int:pk>/',
        views.remove_product,
        name='remove_product',
    ),
]
