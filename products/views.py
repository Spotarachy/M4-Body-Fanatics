from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """This view will show our products page & it will include both the search &sorting """

    products = Product.objects.all()

    context = {
        'products': products
    }   
    return render(request, 'products/products.html', context)

def products_detail(request):
    """This view will get specific product information """

    products = get_objects_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }   
    return render(request, 'products/products.html', context)