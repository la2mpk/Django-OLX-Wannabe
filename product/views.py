from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Product, ProductImages, Category
from django.db.models import Q


def home(request):
    categories = Category.objects.all().order_by('-category_name')
    context = {'categories': categories}
    return render(request, 'base.html', context)


def product_list(request, category_slug=None):
    products = Product.objects.all()
    category = None

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query)
        )

    products = products.order_by('-created')

    # A todas las categorias le agrego un atributo que contabiliza 
    # cuantos productos pertenecen a cada categoria
    categories = Category.objects.annotate(num_products=Count('product'))

    paginator = Paginator(products, 2) # Muestra 2 elementos por página
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {'products': products, 'category': category, 'categories': categories}

    return render(request, 'product/product_list.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'images': images}
    return render(request, 'product/product_detail.html', context)
