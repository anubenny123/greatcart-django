from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Product
from category.models import Category


def store(request, category_slug=None):
    categories = None
    products   =None
    if category_slug!=None:
        categories = get_object_or_404(Category,slug=category_slug)
        products   = Product.objects.filter(category=categories,is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    
    return render(request, 'store.html', context)

def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e 
    context ={
        'single_product':single_product
    }
    return render(request,'product_detail.html',context)











# def products_by_category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category, is_available=True)
#     context = {
#         'category': category,
#         'products': products,
#     }
#     return render(request, 'store.html', context)
