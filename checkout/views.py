from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import setting

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Shoping bag is empty')
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 
        'sk_test_51L3yfhH1FgX9COuG6xeKMo7vFSh2XMWPyKIKPXE1KmnlEFE1uiWG73jgNb2ZgTJ1DTmJYbJskzAs2da2kw0L4RR500qNGJwq33',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)