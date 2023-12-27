from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.functions import Lower


from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    category = ''
    sort = None
    direction = 'asc'

    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            category = request.GET['category']

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            query = ''
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

    context = {
        'products': products,
        'current_categories': categories,
        'category': f"{category} products",
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product.id)

    paginator = Paginator(related_products, 4)
    page = request.GET.get('page')

    try:
        related_products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        related_products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page.
        related_products = paginator.page(paginator.num_pages)

    context = {
        'product': product,
        'related_products': related_products
    }

    return render(request, 'products/product_detail.html', context)
