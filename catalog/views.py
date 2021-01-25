from django.shortcuts import render

from .models import Product, Category


def product_list(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'products': Product.objects.filter(category=category),
    }

    return render(request, 'catalog/category.html', context)

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }

    return render(request, 'catalog/product.html', context)