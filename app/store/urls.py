from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path(
        '',
        views.IndexPageTemplateView.as_view(),
        name='index',
    ),
    path(
        'products/',
        views.ProductsListView.as_view(),
        name='products',
    ),
    path(
        'products/<int:pk>/',
        views.ProductDetailView.as_view(),
        name='product',
    ),
    path(
        'products/add/',
        views.AddProductCreateView.as_view(),
        name='add_product',
    ),
    path(
        'products/edit/<int:pk>/',
        views.EditProductUpdateView.as_view(),
        name='edit_product',
    ),
    path(
        'products/delete/<int:pk>/',
        views.ProductDeleteView.as_view(),
        name='remove_product',
    ),
    path(
        'qwerty',
        views.MyView.as_view(),
    ),
]
