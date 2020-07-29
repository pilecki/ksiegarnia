from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Genre, ComingSoon
from .forms import ProductForm, ComingSoonForm

# Create your views here.


def all_products(request):

    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    genres = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'genres': genres,

    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):

    """ Add a product to the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):

    """ Edit a product in the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    """ Delete a product from the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))


def coming_soon(request):

    """ A view to show new books coming soon  """

    comingSoon = ComingSoon.objects.all()

    context = {
        'comingSoon': comingSoon,
    }
    return render(request, 'products/coming.html', context)


def coming_soon_detail(request, product_id):

    """ A view to show individual product details """

    comingSoon = get_object_or_404(ComingSoon, pk=product_id)

    context = {
        'comingSoon': comingSoon,
    }

    return render(request, 'products/coming_soon_detail.html', context)


@login_required
def edit_coming_soon(request, product_id):

    """ Edit a product in the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    comingSoon = get_object_or_404(ComingSoon, pk=product_id)

    if request.method == 'POST':
        form = ComingSoonForm(request.POST, request.FILES, instance=comingSoon)
        if form.is_valid():
            form.save()
            return redirect(reverse('coming_soon_detail', args=[product_id]))
    else:
        form = ComingSoonForm(instance=comingSoon)

    template = 'products/edit_coming_soon.html'
    context = {
        'form': form,
        'comingSoon': comingSoon,
    }

    return render(request, template, context)


@login_required
def delete_coming_soon(request, product_id):

    """ Delete a product from the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    comingSoon = get_object_or_404(ComingSoon, pk=product_id)
    comingSoon.delete()
    return redirect(reverse('products'))


@login_required
def add_coming_soon(request):

    """ Add a product to the bookstore """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ComingSoonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_coming_soon'))
    else:
        form = ComingSoonForm()

    template = 'products/add_coming_soon.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
