from django.shortcuts import render
from .models import Product

def all_products(request):
    """This view will show our products page & it will include both the search &sorting """

    products = Product.objects.all()

    context = {
        'products': products
    }   
    return render(request, 'products/products.html', context)