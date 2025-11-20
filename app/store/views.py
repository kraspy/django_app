from django import views
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import AddProductForm, RemoveProductForm
from .models import Category, Product
from .tasks import add_product

class IndexPageTemplateView(TemplateView):
    template_name = 'store/index.html'

class ProductsListView(ListView):
    model = Product
    paginate_by = 8
    template_name = 'store/products.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'

class AddProductCreateView(CreateView):
    model = Product
    template_name = 'store/add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('store:products')

    def form_valid(self, form):
        response = super().form_valid(form)
        add_product.delay(self.object.name)
        return response

class EditProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/edit_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('store:product')

    def get_success_url(self):
        return reverse_lazy('store:product', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/remove_product.html'
    success_url = reverse_lazy('store:products')


class MyView(View):
    def get(self, request):
        return HttpResponse(request)
