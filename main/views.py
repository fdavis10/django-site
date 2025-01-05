from django.shortcuts import render, get_object_or_404
from .models import Products, Category

def popular_list(request):
    products = Products.objects.filter(available=True)[:3]
    return render(request, 'main/index/index.html',
                  {"products":products})


def product_detail(request, slug):
    product = get_object_or_404(Products,
                                slug = slug,
                                available=True)
    
    return render(request,
                  'main/product/detail.html',
                  {'product':product})
