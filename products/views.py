from django.shortcuts import render

def all_products(request):
    """ A view to return the index page """

    return render(request, 'products/products.html')

def product_detail(request):
    """ A view to show individual product details """

    return render(request, 'products/product_detail.html')
