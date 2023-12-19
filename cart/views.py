from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from products.models import Product
from programs.models import Program



# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    item_type = request.POST.get('item_type')

    if item_type == 'product':
        product = get_object_or_404(Product, pk=item_id)
    else:
        product = get_object_or_404(Program, pk=item_id )

    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()) and quantity:
        cart[item_id] += int(quantity)
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = 1
        messages.success(request, f'Added {product.name} to your cart')


    request.session['cart'] = cart
    return redirect(redirect_url)
