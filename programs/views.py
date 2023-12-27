from django.shortcuts import render,reverse, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from products.models import Category
from .models import Program
from cart.contexts import cart_contents


# Create your views here.
def all_programs(request):
    """ A view to show all programs, including sorting and search queries """

    programs = Program.objects.all()
    query = None
    categories = None

    if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            programs = programs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('programs'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        programs = programs.filter(queries)

    context = {
        'programs': programs,
        'search_term': query,
        'current_categories': categories
    }

    return render(request, 'programs/programs.html', context)


def program_detail(request, program_id):
    """ A view to show individual product details """

    program = get_object_or_404(Program, pk=program_id)
    related_products = Program.objects.filter(category=program.category).exclude(pk=program.id)

    if request.user.is_authenticated:
        if hasattr(request.user, 'userprofile'):
            orders = request.user.userprofile.orders.all()
        else:
            orders = []
    else:
        orders = []


    purchased = False
    for order in orders:
        for item in order.lineitems.all():
            if item.content_object.id == program_id:
                purchased = True

    current_cart = cart_contents(request)
    in_cart = any(item['product'].id == program.id for item in current_cart['cart_items'])


    print(in_cart)

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
        'program': program,
        'related_products': related_products,
        "purchased" : purchased,
        'in_cart': in_cart
    }


    return render(request, 'programs/program_detail.html', context)
