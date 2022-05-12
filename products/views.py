from django.shortcuts import render, redirect, reverse,  get_object_or_404 
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower


from .models import Product, Category

def all_products(request):
    """This view will show our products page & it will include both the search &sorting """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = categories.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search was Sent!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    name_descending = f'{sort}_{direction}'
    # current_sorting 

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'name_descending' : name_descending,
    }  
    # will have to fix it here all  /\ 

    return render(request, 'products/products.html', context)

def products_detail(request, product_id):
    """This view will get specific product information """
    print(request)
    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }   
    return render(request, 'products/products_detail.html', context)