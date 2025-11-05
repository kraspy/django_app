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

# # Create your views here.
# def page_index(request):
#     return render(request, 'store/index.html')


class IndexPageTemplateView(TemplateView):
    template_name = 'store/index.html'


# def products(request):
#     products = Product.objects.all()
#     paginator = Paginator(products, 8)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,
#     }

#     return render(request, 'store/products.html', context)


class ProductsListView(ListView):
    model = Product
    paginate_by = 8
    template_name = 'store/products.html'


# def product(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     context = {
#         'product': product,
#     }

#     return render(request, 'store/product.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'


# def add_product(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('store:index')

#     else:
#         form = AddProductForm()

#     return render(request, 'store/add_product.html', {'form': form})


class AddProductCreateView(CreateView):
    model = Product
    template_name = 'store/add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('store:products')


# def edit_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     if request.method == 'POST':
#         form = AddProductForm(instance=product)

#         if form.is_valid():
#             form.save()
#             return redirect('store:product', pk=pk)

#     else:
#         form = AddProductForm(instance=product)

#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, 'store/edit_product.html', context)


class EditProductUpdateView(UpdateView):
    model = Product
    template_name = 'store/edit_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('store:product')

    def get_success_url(self):
        return reverse_lazy('store:product', kwargs={'pk': self.object.pk})


# def remove_product(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     if request.method == 'POST':
#         form = RemoveProductForm(request.POST)
#         if form.is_valid():
#             product.delete()
#             return redirect('store:products')
#     else:
#         form = RemoveProductForm()

#     context = {
#         'form': form,
#         'product': product,
#     }

#     return render(request, 'store/remove_product.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/remove_product.html'
    success_url = reverse_lazy('store:products')


class MyView(View):
    def get(self, request):
        return HttpResponse(request)
