from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.views import View
from django.conf import settings
from .forms import OrderForm

from .models import Order, OrderLineItem
from products.models import Product
from programs.models import Program




from cart.contexts import cart_contents

import stripe


# Create your views here.
class CheckoutView(View):
    template_name = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
     
    def get(self, request, *args, **kwargs):  
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        total = current_cart['total']

        stripe_total = round(total * 100)

        order_form = OrderForm()
        stripe.api_key = self.stripe_secret_key

        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        for item_id, item_data in cart.items():
            print(item_data)

        context = {
            'order_form': order_form,
            'stripe_public_key': self.stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})


        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():



                try:
                    if item_data['product_type'] == 'product':
                        product = Product.objects.get(id=item_id)
                    else:
                        product = Program.objects.get(id=item_id)
                    
                    
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data['quantity'],
                        )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double-check your information.')
            return redirect(reverse('checkout'))  # Redirect back to checkout page with error messages

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)