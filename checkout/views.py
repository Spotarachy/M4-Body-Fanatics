from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Shoping bag is empty')
        return redirect(reverse('products'))
    order_from = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_from,
    }

    return render(request, template, context)