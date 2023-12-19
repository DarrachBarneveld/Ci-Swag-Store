from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Category
from .models import Program

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

    context = {
        'programs': programs,
        'current_categories': categories
    }

    return render(request, 'programs/programs.html', context)


def program_detail(request, program_id):
    """ A view to show individual product details """

    program = get_object_or_404(Program, pk=program_id)
    related_products = Program.objects.filter(category=program.category).exclude(pk=program.id)

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
        'related_products': related_products
    }


    return render(request, 'programs/program_detail.html', context)
