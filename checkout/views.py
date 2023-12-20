from django.shortcuts import render
from .forms import OrderForm

# Create your views here.
def checkout(request):
    template = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
