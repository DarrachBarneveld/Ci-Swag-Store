from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from programs.models import Program

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if int(item_id) >= 26:
            product = get_object_or_404(Program, pk=item_id)
            product_type = 'program'
        else:
            product = get_object_or_404(Product, pk=item_id)
            product_type = 'product'

        quantity = item_data.get('quantity', 0)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': int(item_id),
            'quantity': quantity,
            'product': product,
            'product_type': product_type
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
