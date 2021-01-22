from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .form import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ICPtwAMDP3ttg636pKJnVIUlxQU6znYCmfm9pZnFPqwrBIW6iyyZGHJbX2EiP3tJ27QQgXmblTccIGTUEeutr3b007qtbsbMN',
    }

    return render(request, template, context)
