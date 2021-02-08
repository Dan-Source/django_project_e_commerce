from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models

from watson import search as watson

from .models import Product, Category

class ProductListView(generic.ListView):

    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset

class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    paginate_by = 4
    
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


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

product_list = ProductListView.as_view()
category = CategoryListView.as_view()