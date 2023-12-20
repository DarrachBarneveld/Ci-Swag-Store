from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm


from cart.contexts import cart_contents

import stripe


# Create your views here.
def checkout(request):
    template = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_cart = cart_contents(request)

    total = current_cart['total']
    stripe_total = round(total * 100)


    print(stripe_total)




    order_form = OrderForm()
    stripe.api_key = stripe_secret_key

    print(stripe_secret_key)

    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
