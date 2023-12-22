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
        else:
            product = get_object_or_404(Product, pk=item_id)

        total += item_data * product.total_final_price
        product_count += item_data
        cart_items.append({
            'item_id': int(item_id),
            'quantity': item_data,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
