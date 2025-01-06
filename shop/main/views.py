from django.shortcuts import render, get_object_or_404
from .models import Products, Category

def popular_list(request):
    products = Products.objects.filter(available=True)[:5]
    return render(request, 'main/index/index.html',
                  {"products":products})


def product_detail(request, slug):
    product = get_object_or_404(Products,
                                slug = slug,
                                available=True)
    
    return render(request,
                  'main/product/detail.html',
                  {'product':product})


def product_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)
    return render(request, 
                  'main/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'producsts': products})