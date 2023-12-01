from django.shortcuts import render, get_object_or_404

from main_app.models import Product


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog_home(request):
    return render(request, "blog-home.html")


def blog_post(request):
    return render(request, "blog-post.html")


def base(request):
    return render(request, "base.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")


def portfolio_item(request):
    return render(request, "portfolio-item.html")


def portfolio_overview(request):
    return render(request, "portfolio-overview.html")


def pricing(request):
    return render(request, "pricing.html")


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products': products})


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product.html', {'product': product})
