from django.shortcuts import get_object_or_404, render

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
