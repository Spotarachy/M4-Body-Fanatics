from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Shoping bag is empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L3yfhH1FgX9COuGJP1j9lYeMGEJPxUqB8iau8noRZymJ8CjjZysSMxWBU6ARZ2NvLJaAfwifpnyjba1k64MlcvU004EX1Lbgz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)