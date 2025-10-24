from django.shortcuts import get_object_or_404, redirect, render

from .forms import AddProductForm, RemoveProductForm
from .models import Category, Product


# Create your views here.
def page_index(request):
    return render(request, 'store/index.html')


def products(request):
    context = {
        'products': Product.objects.all(),
    }

    return render(request, 'store/products.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'store/product.html', context)


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store:index')

    else:
        form = AddProductForm()

    return render(request, 'store/add_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = AddProductForm(instance=product)

        if form.is_valid():
            form.save()
            return redirect('store:product', pk=pk)

    else:
        form = AddProductForm(instance=product)

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'store/edit_product.html', context)


def remove_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = RemoveProductForm(request.POST)
        if form.is_valid():
            product.delete()
            return redirect('store:products')
    else:
        form = RemoveProductForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'store/remove_product.html', context)
