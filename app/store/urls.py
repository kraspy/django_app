from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.page_index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:pk>/', views.product, name='product'),
]
