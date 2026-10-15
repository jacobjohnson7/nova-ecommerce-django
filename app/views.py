
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Product, Category, Banner
from .forms import RegisterForm


def home(request):
    banners = Banner.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(
        is_active=True,
        is_featured=True
    ).select_related("category")

    return render(request, "store/home.html", {
        "banners": banners,
        "categories": categories,
        "products": products,
    })


def products(request):
    items = Product.objects.filter(is_active=True).select_related("category")
    categories = Category.objects.filter(is_active=True)
    search = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")

    if search:
        items = items.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search)
        )

    if category:
        items = items.filter(category__slug=category)

    return render(request, "store/products.html", {
        "products": items,
        "categories": categories,
        "search": search,
        "selected_category": category,
    })


def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:4]

    return render(request, "store/product_detail.html", {
        "product": product,
        "related_products": related_products,
    })


def register(request):
    if request.user.is_authenticated:
        return redirect("account")

    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account has been created.")
        return redirect("account")

    return render(request, "store/register.html", {
        "form": form
    })


@login_required
def account(request):
    return render(request, "store/account.html")
