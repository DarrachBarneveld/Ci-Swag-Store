from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages

from products.models import Product
from programs.models import Program



# Create your views here.
def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))

    if int(item_id) >= 26:
        product = get_object_or_404(Program, pk=item_id)
    else:
        product = get_object_or_404(Product, pk=item_id )

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


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')


    if int(item_id) >= 26:
        product = get_object_or_404(Program, pk=item_id)
    else:
        product = get_object_or_404(Product, pk=item_id )

    try:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
